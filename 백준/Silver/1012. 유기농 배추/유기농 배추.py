import sys
sys.setrecursionlimit(10**7)

case = int(sys.stdin.readline())


def dfs(x, y): # weight, height

    if field[y][x] == 0:
        return
    elif field[y][x] == 1:
        field[y][x] = 0



    left, right = x - 1, x + 1
    up, down = y + 1, y - 1

    # 오른쪽 탐색
    if right >= len(field[0]):
        pass
    else:
        dfs(right, y)

    # 왼쪽 탐색
    if left < 0:
        pass
    else:
        dfs(left, y)

    # 위쪽 탐색
    if up >= len(field):
        pass
    else:
        dfs(x, up)
    # 아래쪽 탐색
    if down < 0:
        pass
    else:
        dfs(x, down)

for _ in range(case):
    # m = 가로/ n = 세로
    # k = 배추의 개수
    m, n, k = map(int, sys.stdin.readline().split())


    # 배추밭
    field = [[0 for i in range(m)] for j in range(n)]
    # print(field)
    # print(len(field[0])) # 가로 = m
    # print(len(field))   # 세로 = n


    # 배추 위치 표시하기
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1  # y = 세로, x = 가로
        # print(field)

    cnt = 0
    # 탐색 시작
    for h in range(n):
        for w in range(m):
            # print(f"w = {w}, h = {h}")

            if field[h][w] == 1:
                dfs(w, h)
                cnt += 1

    print(cnt)
