n, m = map(int, input().split())
coin = sorted(list(map(int, input().split())))

T = [[0]*(n+1) for _ in range(m)]

#初期化
T[:][0] = 0
for j in range(n+1):
    T[0][j] = j

for i in range(1,m):
    for j in range(1,n+1):
        if j >= coin[i]:
            T[i][j] = min(T[i-1][j], T[i][j-coin[i]]+1)
        else:
            T[i][j] = T[i-1][j]
print(T[m-1][n])
