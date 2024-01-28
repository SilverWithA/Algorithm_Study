import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

std, edge, x = map(int, input().split())
graph = [[] for _ in range(std + 1)]
for _ in range(edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end,weight))

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance = [INF] * (std+1)
    distance[start] = 0

    while Q:
        weight, node = heapq.heappop(Q)
        if distance[node] < weight:
            continue
        for next_node, next_weight in graph[node]:
            alt = weight + next_weight
            if alt < distance[next_node]:
                distance[next_node] = alt
                heapq.heappush(Q, (alt, next_node))
    return distance

res = 0
for i in range(1, std +1):
    go = dijkstra(i)
    come = dijkstra(x)
    res = max(res, go[x] + come[i])
print(res)