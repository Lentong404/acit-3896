import time

before = time.perf_counter()
lst = make_random_list()
lst.sort()              # <-- this is SLOW
result = binary_search(target, lst)
after = time.perf_counter()