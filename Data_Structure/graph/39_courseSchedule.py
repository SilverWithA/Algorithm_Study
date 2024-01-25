import collections
def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)
    print(graph)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문 했던 노드면 True - 가지치기
        if i in visited:
            return True

        traced.add(i)
        # 탐색
        for y in graph[i]:
            if not dfs(y):
                return False
            traced.remove(i)
            visited.add(i)

            return True
    for x in list(graph):
        if not dfs(x):
            return False
    return True

print(canFinish(2,[[1,0],[0,1]]))