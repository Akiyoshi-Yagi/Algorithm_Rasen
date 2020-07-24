from heapq import heappush, heappop, heappushpop, heapreplace, heapify

n, e = map(int, input().split())
#edge_listに各辺の情報を格納する
edge_list = [[] for i in range(n)]
for _ in range(e):
    s, t, u = map(int, input().split())
    edge_list[s].append([u, t])
    edge_list[t].append([u, s])

def dijkstra(edges, start):
    #startの点から各頂点までの最短距離
    d = [float("inf")] * n
    used = [False] * n
    d[start] = 0
    used[start] = True
    #各ノードへのstartからのcostを記録するlistを導入
    node_cost_list = []

    for e in edges[start]:
        heappush(node_cost_list, e)
    while len(node_cost_list):
        min_cost_node = heappop(node_cost_list)
        if used[min_cost_node[1]]:
            continue
        v = min_cost_node[1]
        d[v] = min_cost_node[0]
        used[v] = True
        for z in edges[v]:
            if not used[z[1]]:
                heappush(node_cost_list, [z[0]+d[v], z[1]])
    return d


if __name__ == "__main__":
    for k in range(n):
        print(dijkstra(edge_list, k))

