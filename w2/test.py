import time
import statistics
  
n = 10
num_trials = 1000
times = []

def make_list(n):
  return list(range(n))

def make_dict(n):
    dct={}
    return {i: i for i in range(n)}

#Scenario 1 - Add with lst.append(0, -77)
for i in range(num_trials):
    lst = make_list(n)             
    before = time.perf_counter()
    lst.insert(0, -77) 
    after = time.perf_counter()
    delta = after - before
    times.append(delta)

avg_seconds = statistics.mean(times)
avg_microseconds = avg_seconds * 1_000_000
print("Add took", avg_microseconds, "microseconds")


#Scenario 2 - Add with lst.append(-77)
for i in range(num_trials):
    lst = make_list(n)             
    before = time.perf_counter()    
    lst.append(-77) 
    after = time.perf_counter()
    delta = after - before
    times.append(delta)

avg_seconds = statistics.mean(times)
avg_microseconds = avg_seconds * 1_000_000
print("Insert took",avg_microseconds, "microseconds")


#Scenario 3 - Remove using lst.pop(0)
for i in range(num_trials):
    lst = make_list(n)             
    before = time.perf_counter()    
    lst.pop(0)
    after = time.perf_counter()
    delta = after - before
    times.append(delta)

avg_seconds = statistics.mean(times)
avg_microseconds = avg_seconds * 1_000_000
print("Remove took", avg_microseconds, "microseconds")

#Scenario 4 - Remove using lst.pop(0)
for i in range(num_trials):
    lst = make_list(n)             
    before = time.perf_counter()    
    lst.pop()
    after = time.perf_counter()
    delta = after - before
    times.append(delta)

avg_seconds = statistics.mean(times)
avg_microseconds = avg_seconds * 1_000_000
print("Remove took",avg_microseconds, "microseconds")

#Scenario 5 - Check if a number is in a list of n elements
for i in range(num_trials):
    lst = make_list(n)      
    present = n - 1        
    before = time.perf_counter()
    # 'In' does a linear search
    present in lst
    after = time.perf_counter()
    delta = after - before
    times.append(delta)

avg_seconds = statistics.mean(times)
avg_microseconds = avg_seconds * 1_000_000
print("Present took",avg_microseconds, "microseconds")

#Scenario 6 - Check if a number is not in a list of elements
for i in range(num_trials):
    lst = make_list(n)      
    absent = -1    
    before = time.perf_counter()    
    absent in lst
    after = time.perf_counter()
    delta = after - before
    times.append(delta)

avg_seconds = statistics.mean(times)
avg_microseconds = avg_seconds * 1_000_000
print("Absent took",avg_microseconds, "microseconds")

#'In' checks the keys in a dictionary
