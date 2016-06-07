import random
from datetime import datetime

def insertion_sort(arr):
    sortednums = 0
    for i in range(1, len(arr)):
        left = i-1
        num = arr[i]
        while num < arr[left]:
            arr[left+1] = arr[left]
            arr[left] = num
            if left == 0:
                break
            left -= 1
    return arr

sample = [random.randrange(10000) for x in range(100)]
date1 = datetime.now()
insertion_sort(sample)
date2 = datetime.now()
delta = date2-date1
print delta.microseconds
