from heapq import heapify, heappop, heappush

print("heapしたい数列を入力してください")
arr = list(map(int, input().split()))
arr = list(map(lambda x : x * (-1), arr))
heapify(arr)
heap_arr = [ s * (-1) for s in arr]
print("max_heap表現")
print(heap_arr)

print("挿入したい数を入力してください")
num = int(input())
arr = [ s * (-1) for s in heap_arr]
num = num * (-1)
heappush(arr, num)
heap_arr = [ s * (-1) for s in arr]
print("挿入後のmax_heap")
print(heap_arr)

print("最大値を取り出したい場合はYESを入力してください")
valid = input()
if valid == "YES":
    print((-1)* heappop(arr))
    heap_arr = [s * (-1) for s in arr]
    print("最大値を取り出された後の数列")
    print(heap_arr)

