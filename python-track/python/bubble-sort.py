import random
from datetime import datetime

def bubble_sort(arr):
    unsorted = len(arr)-1
    while unsorted > 0:
        for i in range(unsorted):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        unsorted -= 1
    return arr

sample = [random.randrange(10000) for x in range(100)]
date1 = datetime.now()
print bubble_sort(sample)
date2 = datetime.now()
delta = date2-date1
print delta.microseconds
