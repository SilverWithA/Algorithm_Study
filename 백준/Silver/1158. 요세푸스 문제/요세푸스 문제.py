# 입력
n, k = map(int, input().split())
arr = [i for i in range(1,n+1)]


answer = []
pointer = 0

while len(arr) != 0:
    # 제거될 인덱스
    pointer = ((pointer + k-1) % len(arr))
    
    # 삭제
    answer.append(str(arr.pop(pointer)))

print("<", ", ".join(answer)[:],">",sep="")