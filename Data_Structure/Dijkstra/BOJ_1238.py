import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
# 입력 받기
std, edge, destin = map(int, input().split())
graph = [[] for _ in range(std + 1)]
for _ in range(edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

def dijkstra(start):
    Q = []
    dist = [INF] * (std + 1)
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        time, node = heapq.heappop(Q)
        if dist[node] < time:
            continue

        for next_node, next_time in graph[node]:
            alt = time + next_time
            if dist[next_node] > alt:
                dist[next_node] = alt
                heapq.heappush(Q, (alt, next_node))
    return dist

result = 0
for i in range(1 ,std+1):
    go = dijkstra(i)
    back = dijkstra(destin)
    result = max(result, go[destin]+ back[i])
print(result)



# 예제
# std, edge, destin = 4, 8, 2
# road = [[1, 2, 4],
# [1, 3, 2],
# [1, 4, 7],
# [2, 1, 1],
# [2, 3, 5],
# [3, 1, 2],
# [3,4 , 4],
# [4, 2, 3]]

