import collections
import heapq

def findCheapestPrice(n,flights, src, dst, k):
    graph = collections.defaultdict(list)
    for start,end,price in flights:
        graph[start].append((end,price))
    print(graph)

    # k는 남은 경유지의 수
    Q = [(0, src, k)]
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for next_node, next_price in graph[node]:
                alt = price + next_price
                heapq.heappush(Q, (alt, next_node, k-1))
    return -1
print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
                        0,3,1))