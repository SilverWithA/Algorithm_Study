# import itertools
# import math
# def solution(numbers):
    

#     numbers = list(numbers)
#     answer = []
#     # 순열(permutations) 사용
#     for i in range(len(numbers)+1):
#         answer = itertools.permutations(numbers,i)
        
    
#     # 나의 풀이---------------------------------
#     answer = list(map(''.join,list(answer)))
    
#     # 1의 자리 숫자 추가
#     answer += numbers
#     answer = list(set(map(int,answer)))
#     # -------------------------------------------
#     print("answer: ",answer)
    
    
    
    
    
#     # 소수찾기
#     prime_cnt = 0
#     for num in answer:
#         if num < 2:
#             continue
#         check = True
#         for i in range(2,int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 check = False
#                 break
#         if check:
#             prime_cnt += 1

#     return prime_cnt
    

# #     # 소수 찾기
# #     prime_cnt = 0
# #     for num in answer:
# #         if num < 2:
# #             continue
# #         if num == 2 or num ==3 or num ==5:
# #             prime_cnt += 1
# #             continue
# #         # print("num: ", num)
# #         for i in range(2, int(math.sqrt(num)) + 1):
# #             # print(i,prime_cnt)
# #             if num % i == 0:
# #                 break
# #         else:        
# #             # print("소수발견. ")
# #             prime_cnt += 1
# #     return prime_cnt



from itertools import permutations

def solution(numbers):
    answer = []                                   
    nums = [n for n in numbers]                   # numbers를 하나씩 자른 것
    per = []                                      
    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))        # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환

    for n in new_nums:                            # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                 # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if n % i == 0:                        # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)                      # 소수일경우 answer 배열에 추가

    return len(set(answer)) 