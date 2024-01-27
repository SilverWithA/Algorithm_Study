import collections
import heapq
def networkDelayTime(times, n,k):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    min_heap = [(0, k)]
    visited = set()
    distance = {i: float('inf') for i in range(1, n + 1)}
    distance[k] = 0

    while min_heap:
        print("min_heap: ",min_heap)
        time, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            print("visited: ",visited)

        for next_node, next_time in graph[node]:
            if time + next_time < distance[next_node]:
                distance[next_node] = time + next_time
                heapq.heappush(min_heap, (time + next_time, next_node))


    return max(distance.values()) if len(visited) == n else -1

    # 인접 리스트 형태의 그래프로 만들어주기
    # graph = collections.defaultdict(list)
    # for start_node, end_node, time in times:
    #     graph[start_node].append((end_node, time))
    # print(graph)
    #
    # # 큐를 이용해 탐색 시작
    # # 소요시간 = 0 , 시작 노드 = k
    # Queue = [(0,k)]
    # # 각 노드 간 최소 소요 시간을 저장할 변수
    # dist = collections.defaultdict(int)
    # while Queue:
    #     time, node = heapq.heappop(Queue)
    #     print("time, node: ",time, node)
    #     if node not in dist:
    #         dist[node] = time
    #         print("dist: ", dist)
    #         # node를 기준으로 bfs 탐색
    #         for next_node, next_time in graph[node]:
    #             print("next_node, next_time: ", next_node, next_time)
    #             alt = time + next_time
    #             heapq.heappush(Queue ,(alt, next_node))
    #             print("Queue: ", Queue)
    #             print()
    #
    # if len(dist) == n:
    #     return max(dist.values())
    # return -1

print(networkDelayTime([[1,2,1],[2,1,3]],2,2))