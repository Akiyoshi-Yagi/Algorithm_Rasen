v, e = map(int, input().split())

inf = float("inf")

#edgesをdp的に用いる
edges = [[inf]*v for _ in range(v)]
for _ in range(e):
    s, t, d = map(int, input().split())
    edges[s][t] = d

for w in range(v):
    edges[w][w] = 0

for k in range(v):
    for i in range(v):
        for j in range(v):
            edges[i][j] = min(edges[i][j], edges[i][k]+edges[k][j])


if any(edges[i][i] < 0 for i in range(v)):
    print("NEGATIVE CYCLE")
else:
    for x in edges:
        x = ["INF" if y == inf else str(y) for y in x]
        print(" ".join(x))

