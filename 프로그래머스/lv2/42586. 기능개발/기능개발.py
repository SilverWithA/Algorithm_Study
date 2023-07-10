# 문제 이해
from collections import deque

def solution(progresses, speeds):
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    answer_count= []
    n = 1
    

    while progresses:   # 개발해야할 기능이 있을 때까지 반복
        
        # n일차 개발 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        # print(f"{n}일차 개발 현황: ", progresses)

        n += 1
        
        # 최우선순위 개발이 완료되었을 경우
        cnt = 0
        while progresses[0] >=100:
            cnt += 1
            
            progresses.popleft()
            speeds.popleft()
            
            if len(progresses) ==0:
                break
            print("개발 완료된 기능: ", answer)
        
        if cnt != 0:
            answer_count.append(cnt)
        
    return answer_count
    