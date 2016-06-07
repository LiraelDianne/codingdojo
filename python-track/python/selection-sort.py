import random
from datetime import datetime

def selection_sort(arr):
    ops = 0
    sortednums = 0
    while sortednums < len(arr)/2:
        mindex = sortednums
        maxdex = sortednums
        for i in range(sortednums+1, len(arr)-sortednums):
            ops += 1
            if arr[i] < arr[mindex]:
                mindex = i
            if arr[i] > arr[maxdex]:
                maxdex = i
        arr[sortednums], arr[mindex] = arr[mindex], arr[sortednums]

        if maxdex == sortednums:
            arr[mindex], arr[len(arr)-1-sortednums] = arr[len(arr)-1-sortednums], arr[mindex]
        else:
            arr[maxdex], arr[len(arr)-1-sortednums] = arr[len(arr)-1-sortednums], arr[maxdex]
        sortednums += 1
    print "ops:", ops
    return arr


sample = [random.randrange(10000) for x in range(10000)]
date1 = datetime.now()
selection_sort(sample)
date2 = datetime.now()
delta = date2-date1
print delta.microseconds
