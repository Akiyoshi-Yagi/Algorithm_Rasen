n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

dp = [0]*n

for i in range(n):
    dp[i] = 1
    for j in range(0,i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
