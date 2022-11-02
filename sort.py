from random import randrange
import time

def bubbleSort(a):
    n = len(a)
    for i in range(n-1, 0, -1): # n-1, n-2, ..., 1
        for j in range(i):
            if a[j] > a[j + 1]: # a[j], a[j + 1] are out of order.
                a[j], a[j + 1] = a[j + 1], a[j]

# Build an array of n random numbers, and sort them
def test(n):
    a = []
    for i in range(1000):
        a.append(randrange(1000))
    print(a)
    start = time.time()
    bubbleSort(a)
    print(a)
    return time.time() - start
