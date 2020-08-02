arr = list(map(int, input().split()))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        v = arr[i]
        while j >= 0 and v < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = v
    print(arr)

insertion_sort(arr)
