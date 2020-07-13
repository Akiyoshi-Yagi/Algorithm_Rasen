n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

def binary_search(array, target):
    head = 0
    tail = len(array) -1
    while head <= tail:
        mid = (head+tail) // 2
        comp = array[mid]
        if comp > target:
            tail = mid - 1
        elif comp < target:
            head = mid + 1
        else:
            return True
    return False

ans = 0
for a in t:
    if binary_search(s,a):
        ans += 1
    else:
        continue

print(ans)

