import collections
import heapq
def networkDelayTime(times, n,k):

    # 인접 리스트 형태의 그래프로 만들어주기
    graph = collections.defaultdict(list)
    for start_node, end_node, time in times:
        graph[start_node].append((end_node, time))
    print(graph)

    # 큐를 이용해 탐색 시작
    # 소요시간 = 0 , 시작 노드 = k
    Queue = [(0,k)]
    # 각 노드 간 최소 소요 시간을 저장할 변수
    dist = collections.defaultdict(list)
    while Queue:
        time, node = heapq.heappop(Queue)
        print("time, node: ",time, node)
        if node not in dist:
            dist[node]= time
            print("dist: ", dist)
            # node를 기준으로 bfs 탐색
            for next_node, next_time in graph[node]:
                print("next_node, next_time: ", next_node, next_time)
                alt = time + next_time
                heapq.heappush(Queue ,(alt, next_node))
                print("Queue: ", Queue)
                print()

    if len(dist) == n:
        return max(dist.values())
    return -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))