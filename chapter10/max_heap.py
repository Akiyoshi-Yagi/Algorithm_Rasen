from heapq import heapify, heappop, heappush

arr = list(map(int, input().split()))
#MAXheapの時は、-1をかける
arr = list(map(lambda x : x * (-1), arr))
heapify(arr)
heap_arr = [ s * (-1) for s in arr]
print(heap_arr)

