from heapq import heappush, heappop, heappushpop, heapreplace, heapify

n, e, k= map(int, input().split())


#edge_listに各辺の情報を格納する
#無向ver
edge_list = [[] for i in range(n)]
for _ in range(e):
    s, t, u = map(int, input().split())
    edge_list[s].append([u, t])

    #これは、グラフの入力方法によって必要かどうか変わってくるので注意！！！(有向グラフの場合いらない）
    #edge_list[t].append([u, s])


#隣接行列及びスタートを与えると、各頂点までの最短経路を算出するダイクストラ関数
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
        print(used)
        weight, node= heappop(node_cost_list)
        #heapにpushされた時点ではused=Falseだったけど、popされた時にはTrueに変わってしまっているものを除くため。
        if used[node]:
            continue
        d[node] = weight
        used[node] = True
        for z in edges[node]:
            if not used[z[1]]:
                heappush(node_cost_list, [z[0]+d[node], z[1]])
    return d


if __name__ == "__main__":
    for i in dijkstra(edge_list,k):
        if i == float("inf"):
            print("INF")
        else:
            print(i)


'''
4 6 1
0 1 1
0 2 4
2 0 1
1 2 2
3 1 1
3 2 5
'''
