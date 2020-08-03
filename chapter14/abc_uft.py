#https://atcoder.jp/contests/abc097/tasks/arc097_b

class UnionFindTree():

    def __init__(self, n):
        #木全体の要素数
        self.n  = n
        #root[x]<0ならそのノードが根でありその値が木の要素数
        self.root = [-1] * (n+1)
        #ランク
        self.rank = [1] * (n+1)

    def find_root(self,x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self,x,y):
        return self.find_root(x) == self.find_root(y)

    def count_node(self,x):
        return -1 * self.root[self.find_root(x)]


n, m = map(int, input().split())
uft = UnionFindTree(n)

p_arr = list(map(int, input().split()))

for _ in range(m):
    x, y = map(int, input().split())
    uft.unite(x, y)

ans = 0
for index, num in enumerate(p_arr):
    if uft.is_same(index+1, num):
        ans += 1
print(ans)

