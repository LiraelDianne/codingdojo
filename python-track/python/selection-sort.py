import random
from datetime import datetime

def selection_sort(arr):
    ops = 0
    sortednums = 0
    while sortednums < len(arr)-1:
        mindex = sortednums
        for i in range(sortednums+1, len(arr)):
            ops += 1
            if arr[i] < arr[mindex]:
                mindex = i
        arr[sortednums], arr[mindex] = arr[mindex], arr[sortednums]
        sortednums += 1
    print ops
    return arr

sample = [random.randrange(10000) for x in range(10000)]
date1 = datetime.now()
selection_sort(sample)
date2 = datetime.now()
delta = date2-date1
print delta.microseconds
