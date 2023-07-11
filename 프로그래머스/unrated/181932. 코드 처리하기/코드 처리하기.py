def solution(code):
    code = list(code)
    ret = ""
    mode = 0 
    
    for i in range(len(code)):
        
        # 모드 변경
        if code[i]=='1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
        
        
        # 코드 처리
        if ((i+mode) % 2==0):
            if code[i] =='1':
                continue
                
            ret += code[i]
    
    if ret:
        return ret
    else:
        return "EMPTY"



#---------------------- < 다른 풀이 > ------------------------------
# def solution(code):
#     answer = ''

#     mode = 0
#     for i in range(len(code)):
#         if code[i] == '1':
#             mode ^= 1
#         else:
#             if i % 2 == mode:
#                 answer += code[i]

#     return answer if answer else 'EMPTY'
