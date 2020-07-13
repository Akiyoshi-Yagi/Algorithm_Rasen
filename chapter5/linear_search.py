n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

ans = 0
for a in s:
    for b in t:
        if a == b:
            ans += 1

print(ans)
