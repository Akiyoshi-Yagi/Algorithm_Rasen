from union_find_tree import UnionFindTree

n, q = map(int, input().split())

uft = UnionFindTree(n)

ans = []
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        uft.unite(x,y)
    elif com == 1:
        if uft.is_same(x,y):
            ans.append(1)
        else:
            ans.append(0)
for j in ans:
    print(j)



'''
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0
'''
