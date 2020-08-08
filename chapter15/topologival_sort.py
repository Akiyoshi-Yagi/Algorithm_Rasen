from collections import deque

v, e = map(int, input().split())
adj = [[] for _ in range( v)]
inflow = [0] * v
for _ in range(e):
    s, t = map(int, input().split())
    inflow[t] += 1
    adj[s].append(t)

def topological_sort(adj, inflow):
    is_visited = [False] * len(inflow)
    res = []

    def bfs(s):
        #sを始点とする
        q = deque([s])
        is_visited[s] = True
        while q:
            p = q.popleft()
            res.append(p)
            for r in adj[p]:
                inflow[r] -= 1
                if (inflow[r] == 0) and (not is_visited[r]):
                    q.append(r)
                    is_visited[r] = True

    for x in range(len(inflow)):
        if (inflow[x] == 0) and (not is_visited[x]):
            bfs(x)
    return res

for i in topological_sort(adj, inflow):
    print(i)

