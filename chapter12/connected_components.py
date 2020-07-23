from collections import defaultdict
import sys
sys.setrecursionlimit(25)

n, m = map(int, input().split())

#コネクションをdefaultdictを使って保存
connect = defaultdict(lambda: [])
for _ in range(m):
    s, t = map(int, input().split())
    connect[s].append(t)
    connect[t].append(s)

#各ノードの属するグループを辞書型で記録
group = {x:None for x in range(n)}

def dfs(node:int, gro:int):
    if group[node] is not None:
        return
    group[node] = gro

    for n in connect[node]:
        dfs(n, gro)

gro = 1
for node in connect.keys():
    dfs(node, gro)
    gro += 1

q = int(input())
ans = []
for _ in range(q):
    x, y = map(int, input().split())
    if group[x] == group[y]:
        ans.append("yes")
    else:
        ans.append("no")

for a in ans:
    print(a)

