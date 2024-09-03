import collections
def solution(edges):
    # 각 정점의 나간 노드/들어온 노드 수 세기
    edges_cnt = collections.defaultdict(lambda: [0,0])
    
    for key, node in edges:
        edges_cnt[key][0] += 1 # 나간 노드의 수 수
        edges_cnt[node][1] += 1 # 들어온 노드의 수
    
    # 정점 탐색
    answer = [0,0,0,0]
    for key, cnt in edges_cnt.items():
        in_node = cnt[1]
        out_node = cnt[0]
        # 생성된 정점
        if out_node >= 2 and in_node == 0:
            answer[0] = key 
        # 막대 그래프의 수
        elif in_node > 0 and out_node == 0:
            answer[2] += 1
        # 8자 그래프의 수
        elif in_node >= 2 and out_node >= 2:
            answer[3] += 1
    answer[1] = edges_cnt[answer[0]][0] - answer[2] - answer[3]
    return answer
        
        
        
        