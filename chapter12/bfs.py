from collections import deque

h, w = map(int, input().split())
maze = [list(input()) for k in range(h)]

def bfs(start, goal):
    queue = deque([start])
    visited = [[0] * w for u in range(h)]

    while  len(queue) > 0:
        now_loc = queue.popleft()
        cx = now_loc[0]
        cy = now_loc[1]
        for d in [[1,0],[-1,0],[0,1],[0,-1]]:
            #nx, nyは次の位置
            #cx, cyは現在の位置
            nx = cx + d[0]
            ny = cy + d[1]

            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != "#" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append([nx, ny])

        if visited[goal[0]][goal[1]] != 0:
            return visited[goal[0]][goal[1]]

    return 0

step = []
for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            continue
        start = [i, j]
        for s in range(h):
            for t in range(w):
                if maze[s][t] == "#":
                    continue
                goal = [s,t]

                step.append(bfs(start, goal))

ans = max(step)
print(ans)
