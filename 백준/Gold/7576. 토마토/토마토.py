import sys
from collections import deque

m,n = map(int, sys.stdin.readline().split())

box = []
for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            q.append((x, y))





while q:
    x,y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                q.append((nx, ny))
res = []
cnt = 0
for i in range(n):
    res.append(max(box[i]))
    for j in range(m):
        if box[i][j] == 0:
            cnt += 1
if cnt == 0:
    print(max(res)-1)
else:
    print(-1)


