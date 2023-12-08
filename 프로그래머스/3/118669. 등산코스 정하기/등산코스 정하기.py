from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    def get_min_intesity():
        
        # 이동 비용 INF값으로 초기화 
        pq = []
        visited = [10000001] * (n+1)
        
        # 출발 노드 세팅하기
        for gate in gates:
            heappush(pq,(0, gate))
            visited[gate] = 0
            
        while pq:
            intensity, node = heappop(pq)
            
            if node in summits_set or intensity > visited[node]:
                continue
            
            for weight, next_node in graph[node]:
                new_intensity = max(weight, intensity)
                
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(pq,(new_intensity, next_node))
                

                                 
        # 모든 도착 노드에 대해 intensity 계산 완료
        # 순서대로 최소 intensity를 갖는 도착지점 구하기
        min_intensity = [0, 10000001]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
                                 
        return min_intensity
    
    summits_set = summits.sort()
    summits_set = set(summits)
    
    graph = defaultdict(list)
    for i, j , w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
        
    return get_min_intesity()