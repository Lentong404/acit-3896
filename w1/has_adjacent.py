def has_adjacent_duplicate(lst):
  for i in range(1, len(lst)):
      if lst[i] == lst[i - 1]:
          return True
  return False

result = has_adjacent_duplicate([3, 8, 8, 2])
print(result)