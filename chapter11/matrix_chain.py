n = int(input())
p = []
for t in range(n):
    a, b = map(int, input().split())
    if t == 0:
        p.append(a)
    p.append(b)

'''
dp[i][j]は、Mi~Mjを計算するための最小の掛け算の回数
'''
dp = [[float('inf')] * (n+1) for j in range(n+1)]
for k in range(n+1):
    dp[k][k] = 0
    dp[0][k] = 0
    dp[k][0] = 0

#lは対角成分からの距離
for l in range(1,n+1):
    for i in range(0,n-l+1):
        j = i + l
        for k in range(0,j-i):
            dp[i][j] = min(dp[i][j], dp[i][i+k] + dp[i+k+1][j] + p[i-1] * p[j] * p[i+k])
print(dp[1][n])


'''
入力
6
30 35
35 15
15 5
5 10
10 20
20 25

出力
15125
'''
