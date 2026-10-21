lst = [5, 3, 8, 1, 4]

def argmin(lst):
    smallest_num = lst[0]
    smallest_ind = 0
    for i, val in enumerate(lst):
        if val < smallest_num:
            smallest_num = val
            smallest_ind = i
            print(smallest_ind)   #prints DURING the run (tracing)
    return smallest_ind

result = argmin(lst)   #this line actually runs the function
print(result)          #this prints the final answer