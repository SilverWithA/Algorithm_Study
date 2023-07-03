import copy
def solution(n, lost, reserve):
    
# lost가 빌릴 수 있는지 결정ㅈ의 우선순위 -> -1인 번 학생에게 먼저 빌리기
    lost_n = list(set(lost) - set(reserve))
    reserve_n = list(set(reserve) - set(lost))
    lost_num = 0
    
    for i in range(len(lost_n)):
        
        if lost_n[i] - 1 in reserve_n:
            reserve_n.remove(lost_n[i]-1)
        elif lost_n[i] + 1 in reserve_n:
            reserve_n.remove(lost_n[i]+1)
        else:
            lost_num += 1
    return (n - lost_num)
            
            
        