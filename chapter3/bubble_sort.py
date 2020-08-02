arr = list(map(int, input().split()))

def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(1, len(arr))[::-1]:
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                change = True
    return arr

print(bubble_sort(arr))
