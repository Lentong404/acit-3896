import time
import statistics
import csv

# ---------- helpers given in the prompt ----------

def make_list(n):
    return list(range(n))

def make_dict(n):
    return {i: i for i in range(n)}

# ---------- binary search (stretch #1) ----------

def binary_search(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# ---------- core timing machinery ----------

def bench(base_factory, op, trials, mutates):
    """
    base_factory: () -> a fresh base object (list/dict) to test against
    op: (obj) -> performs the one thing we're timing
    trials: how many times to repeat
    mutates: True if op changes obj (so we need a fresh copy each trial)
    Returns: list of elapsed times, in MICROSECONDS
    """
    base = base_factory()
    times = []
    for _ in range(trials):
        if mutates:
            # copy happens BEFORE we start the clock -- we don't want to time the copy
            obj = list(base) if isinstance(base, list) else dict(base)
        else:
            obj = base  # safe to reuse, op doesn't change it
        start = time.perf_counter()
        op(obj)
        end = time.perf_counter()
        times.append((end - start) * 1_000_000)  # seconds -> microseconds
    return times

def summarize(times):
    # method="inclusive" clamps to the observed min/max instead of extrapolating
    # past them -- important when trials is small relative to n=100 cut points.
    q = statistics.quantiles(times, n=100, method="inclusive")
    return {
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "p1": q[0],
        "p99": q[98],
    }

# ---------- scenario definitions ----------
# Each returns (name, base_factory, op, mutates) for a given n.

def core_scenarios(n):
    present = n - 1
    absent = -1
    return [
        ("list.insert(0, x)",  lambda: make_list(n), lambda lst: lst.insert(0, -77), True),
        ("list.append(x)",     lambda: make_list(n), lambda lst: lst.append(-77),    True),
        ("list.pop(0)",        lambda: make_list(n), lambda lst: lst.pop(0),         True),
        ("list.pop()",         lambda: make_list(n), lambda lst: lst.pop(),          True),
        ("present in list",    lambda: make_list(n), lambda lst: present in lst,     False),
        ("absent in list",     lambda: make_list(n), lambda lst: absent in lst,      False),
        ("present in dict",    lambda: make_dict(n), lambda dct: present in dct,     False),
        ("absent in dict",     lambda: make_dict(n), lambda dct: absent in dct,      False),
    ]

def binary_search_scenarios(n):
    lst = make_list(n)  # already sorted, since range() is sorted
    targets = {
        "first":  0,
        "middle": n // 2,
        "last":   n - 1,
        "absent": -1,
    }
    scenarios = []
    for label, target in targets.items():
        op = (lambda t: (lambda l: binary_search(l, t)))(target)  # capture t correctly
        scenarios.append((f"binary_search ({label})", lambda lst=lst: lst, op, False))
    return scenarios

# ---------- driver ----------

TRIALS_FOR_N = {
    10: 2000,
    1000: 500,
    1_000_000: 200,
}

def run_all():
    rows = []  # for CSV / printing
    for n, trials in TRIALS_FOR_N.items():
        scenarios = core_scenarios(n) + binary_search_scenarios(n)
        for name, base_factory, op, mutates in scenarios:
            times = bench(base_factory, op, trials, mutates)
            stats = summarize(times)
            rows.append({
                "n": n,
                "scenario": name,
                "trials": trials,
                "mean_us": stats["mean"],
                "median_us": stats["median"],
                "p1_us": stats["p1"],
                "p99_us": stats["p99"],
            })
    return rows

def print_grid(rows):
    header = f'{"n":>9} | {"scenario":<22} | {"mean(us)":>12} | {"median(us)":>12} | {"p1(us)":>12} | {"p99(us)":>12}'
    print(header)
    print("-" * len(header))
    current_n = None
    for r in rows:
        if r["n"] != current_n:
            if current_n is not None:
                print("-" * len(header))
            current_n = r["n"]
        print(f'{r["n"]:>9,} | {r["scenario"]:<22} | {r["mean_us"]:>12,.2f} | '
              f'{r["median_us"]:>12,.2f} | {r["p1_us"]:>12,.2f} | {r["p99_us"]:>12,.2f}')

def save_csv(rows, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    results = run_all()
    print_grid(results)
    save_csv(results, "/mnt/user-data/outputs/benchmark_results.csv")
    print("\nSaved to benchmark_results.csv")
