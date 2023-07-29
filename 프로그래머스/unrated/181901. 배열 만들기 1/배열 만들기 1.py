def solution(n, k):
    
    
    answer = []
    num = 0
    
    
    for i in range(n+1):
        while num+k <= n:
            num += k
            answer.append(num)
    return answer