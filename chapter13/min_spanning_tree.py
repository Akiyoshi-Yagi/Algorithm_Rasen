from heapq import heappush, heappop


def prim_heap(connection):
    used = [False] * len(connection) #i番目のノードがすでに使われたかどうか
    node_heap = []
    for x in connection[0]:
        heappush(node_heap, x)
    used[0] = True
    ans = 0

    while len(node_heap) != 0:
        min_node = heappop(node_heap)
        if used[min_node[1]]:
            continue
        min_node_num = min_node[1]
        used[min_node_num] = True
        for y in connection[min_node_num]:
            if not used[y[1]]:
                heappush(node_heap, y)
        ans += min_node[0]

    return ans

n, v = map(int, input().split())
#[[[cost,node],[]...],[[],[].....],[]
s_connection = [[] for i in range(n)]
for i in range(v):
    s, t, u = map(int, input().split())
    s_connection[s].append([u, t])
    s_connection[t].append([u, s])


if __name__ == "__main__":
    print(prim_heap(s_connection))


'''

#入力
7 9
0 1 1
1 2 2
1 3 3
2 5 10
1 4 7
3 4 1
3 6 5
4 6 8
5 4 5

'''
