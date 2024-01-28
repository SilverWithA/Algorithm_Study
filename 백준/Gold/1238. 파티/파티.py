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
# print(graph)


# 함수로 구성하기
def dijkstra(start):
    q = []
    distance = [INF] * (std + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    return distance

result = 0
for i in range(1 ,std+1):
    go = dijkstra(i)
    back = dijkstra(destin)
    result = max(result, go[destin]+ back[i])
print(result)
