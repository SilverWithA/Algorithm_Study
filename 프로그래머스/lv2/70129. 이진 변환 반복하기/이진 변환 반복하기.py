# 시도(1): 시간초과
# def solution(s):     
#     cnt = 0
#     diff = 0
    
#         n = len(s)
#         s1 = s.replace("0",'')
#         n1 = len(s1)

#         num += (n - n1)
#         print("num: ",num)
        
#         # 10진수 to 2진수
#         s = bin(n1)
#         s = s[2:]
#         print(s)
#         cnt +=1


#         if s == 1:
#             return [cnt, num]
#----------------------------------------------
# 시도(2): 시간초과 줄이기
        
        
def solution(s):
    answer = []
    
    cnt = 0
    rm_cnt = 0
    
    while True:
        if s == '1':
            break
        rm_cnt = rm_cnt + s.count("0")
        s = s.replace("0", "")
        
        s = bin(len(s))[2:]
        
        cnt = cnt + 1
    
    answer = [cnt, rm_cnt]
    
    return answer

    