import collections


def findItinerary(tickets):
    route = []

    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)

    print(graph)
    route, stack = [], ["JFK"]
    # 스택 연산으로 반복하기
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
            # stack[-1]은 반복문을 돌면서 변화함 = 깊이에 따라 노드가 변화하는 것처럼 작동
            # "JFK" 였다가 이 연산에서 'ATL'로 변화함
        route.append(stack.pop())

    return route[::-1]
print(findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))





