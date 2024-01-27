import collections
import heapq

def findCheapestPrice(n,flights, src, dst, k):
    graph = collections.defaultdict(list)
    for start, end, price in flights:
        graph[start].append((end, price))
    print("graph: ",graph)

    # price, 경유지, 시작 노드
    Q = [(0, k+1, src)]
    distance = [float('inf')] * n
    distance[src] = 0
    while Q:
        print()
        print("Q: ",Q)
        print("distance: ", distance)
        price, k, node = heapq.heappop(Q)
        print("node: ",node)
        if k >= 0:
            for next_node, next_price in graph[node]:
                print("next_node: ",next_node)
                alt = price + next_price
                if alt < distance[next_node]:
                    distance[next_node] = alt
                    heapq.heappush(Q, (alt, k - 1, next_node))
    return -1 if distance[dst] == float('inf') else distance[dst]

print(findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],
                        0,2,2))