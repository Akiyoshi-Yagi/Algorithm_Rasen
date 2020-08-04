N,W = map(int, input().split())

weight = []
value = []

for _ in range(N):
    x, y = map(int, input().split())
    value.append(x)
    weight.append(y)

T = [[0]*(W+1) for _ in range(N+1)]
T[:][0] = 0
T[0][:] = [0]*(W+1)

#初期化を上でしてるので、ループを回す範囲に注意！！！
#もしiを0から回し始めると、if分の中で不具合が発生する（i-1=-1)
for i in range(1,N+1):
    for j in range(1,W+1):
        if j >= weight[i-1]:
            T[i][j] = max(T[i-1][j-weight[i-1]] + value[i-1], T[i-1][j])
        else:
            T[i][j] = T[i-1][j]
print(T[N][W])

