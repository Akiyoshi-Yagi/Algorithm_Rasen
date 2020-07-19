from collections import deque
from itertools import islice

array = list(map(int,input().split()))
Q = deque(array)

def merge_sort(a):

    if len(a) == 1:
        return a
    else:
        mid = len(a) // 2
        return merge(merge_sort(deque(islice(a, 0, mid))), merge_sort(deque(islice(a, mid, len(a)))))

def merge(x, y):
    z = deque([])
    while len(x) > 0 and len(y) > 0:
        X = x[0]
        Y = y[0]
        if X < Y:
            z.append(x.popleft())
        elif Y < X:
            z.append(y.popleft())
        elif X == Y:
            z.append(x.popleft())
            z.append(y.popleft())

        if len(x) == 0 or len(y) == 0:
            z = z + x + y
    return z

print(list(merge_sort(Q)))


