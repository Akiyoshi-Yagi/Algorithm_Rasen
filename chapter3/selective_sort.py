arr = list(map(int, input().split()))

def selective_sort(arr):
    for i in range(len(arr)-1):
        min = arr[i]
        min_index = i
        for index in range(i+1,len(arr)):
            if arr[index] < min:
                min = arr[index]
                min_index = index
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selective_sort(arr))
