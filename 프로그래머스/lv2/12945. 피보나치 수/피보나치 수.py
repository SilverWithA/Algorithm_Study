# 단순 재귀를 이용한 피보나치 수열----------------------
# 런타임 에러----------------------------------------

# def solution(n):
#     if n == 0:
#         return 0
#     if n ==1:
#         return 1
#     return solution(n-1) + solution(n-2)


# 동적계획법의 핵심: 반복되는 연산 작업을 저장해두고 꺼내쓰는 것-------
# (1) 재귀 방식-------------------------------------------------


# def solution(n):
#     answer = [0] * n
#     print("answer: ", answer)
    
#     def fibo(n):
#         if n == 0 or n ==1:
#             # print("answer: ", answer)
#             return 1
    
#         if answer[n+1] != 0:
#             # print("answer: ", answer)
#             return answer[n] % 1234567
    
#         answer[n+1] =  fibo(n-2) + fibo(n-1)
#         # print("answer: ", answer)
#         return answer[n] % 1234567
    
#     return fibo(n)

# # (2) for문으로 구현-------------------------------------------------
def solution(n):
    result = [0,1,1] + [0]*(n-2)
    # print(result)
    
    for i in range(3,n+1):
        result[i] = (result[i-2] + result[i-1])%1234567
        # print(result)
        
    return result[n] % 1234567
    
    