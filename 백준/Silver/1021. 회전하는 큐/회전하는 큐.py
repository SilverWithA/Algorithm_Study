from collections import deque

# 입력값 받기
n, m = map(int, input().split())
extract_ele = list(map(int, input().split()))

# 큐 생성
queue = deque([i for i in range(1, n+1)])



calculationCount = 0
# 요소를 이동시키는 방법은? -> pop한걸 append한다
for ele in extract_ele:
    for idx in range(len(queue)):
        
        # 추출할 요소 탐색 
        if queue[idx] == ele:
            
            # 요소가 전체 큐에서 비교적 앞에 위치할때
            if idx < len(queue)/2:
                while queue[0] != ele:
                    # 2번 왼쪽 이동 연산
                    queue.append(queue.popleft())
                    calculationCount += 1
                    
            # 요소가 뒤쪽에 위치할때
            else:
                while queue[0] != ele:
                    # 3번 오른쪽 이동 연산
                    queue.appendleft(queue.pop())
                    calculationCount += 1
                    
    if queue[0] == ele:
        queue.popleft()
    
print(calculationCount)