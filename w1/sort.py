def is_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

result = is_sorted([2, 4, 4, 7, 10])
print(result)