'''
https://atcoder.jp/contests/atc001/tasks/dfs_a
'''
import sys

h, w = map(int, input().split())
maze = [list(input()) for k in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j] == "s":
            sx, sy = i, j
        elif maze[i][j] == "g":
            gx, gy = i,j

stack = [[sx, sy]]
visited = [[0] * w for i in range(h)]
visited[sx][sy] = 1

while stack:
    x, y = stack.pop()
    for s in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx, ny = x+s[0], y+s[1]
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and maze[nx][ny] != "#":
            visited[nx][ny] = 1
            stack.append([nx, ny])
        if visited[gx][gy] == 1:
            print("Yes")
            sys.exit()
print("No")


