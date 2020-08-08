from heapq import heappush, heappop, heappushpop, heapreplace, heapify

#隣接リスト作成
v = int(input())
edge_list = [[] for _ in range(v)]
for i in range(v):
    l = list(map(int, input().split()))
    for j in range(1,l[1]+1):
        edge_list[l[0]].append([l[2*j+1],l[2*j]])

def dijkstra(v, edges, start):
    d = [float("inf")] * v
    d[start] = 0
    hq = []
    for i in edges[start]:
        d[i[1]] = i[0]
        heappush(hq, i)

    while hq:
        x, y = heappop(hq)
        for n in edges[y]:
            alt = d[y] + n[0]
            if d[n[1]] > alt:
                d[n[1]] = alt
                heappush(hq, [alt, n[1]])
    return d

for index, d in enumerate(dijkstra(v, edge_list,0)):
    print(index,d)
