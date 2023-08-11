#  문제 이해하기:
# 1과 2를 이용해 n을 만드는 경우의 수 구하는 문제와 유사
# 동적계획법: 피보나치 수열의 구조임
# n = 5일때 
# (1) 가로로 먼저 하나 배치하는 경우의 수는 n=4의 모든 경우의 수와 동일
# (2) 세로로 먼저 하나 배치하는 경우의 수는 n=3의 모든 경우의 수와 동일

# 따라서 solution(5) = solution(3) + solution(4)


# 1. 재귀를 이용해 풀어보기 -> 입출력케이스는 통과지만 당연히 런타임 에러
# def solution(n):
#     if n == 1 or n==2:
#         return n
#     return solution(n-2) + solution(n-1)

# 2. 동적계획법을 이용해 풀어보기---------------------------------
def solution(n):
    answer=[1,2] + [0]*(n-2)
    for i in range(2,n):
        answer[i] = (answer[i-1] + answer[i-2]) % 1000000007
    return answer[n-1]   
    
    
    