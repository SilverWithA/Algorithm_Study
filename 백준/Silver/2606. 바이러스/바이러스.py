# 틀렸습니다?

import sys
from collections import defaultdict

node = int(sys.stdin.readline())  # 노드의 수
edge = int(sys.stdin.readline())  # 간선의 수

graph = defaultdict(list) # list를 디폴트 값(value)로 갖는 딕셔너리 생성

for _ in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

infected = set()
def dfs(node):
    infected.add(node)

    while graph[node]:
        dfs(graph[node].pop(0))

dfs(1)
print(len(infected)-1)



