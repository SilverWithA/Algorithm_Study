def solution(numLog):
    answer = ''
    
    for i in range(len(numLog)-1):
        
        if numLog[i+1] - 1 == numLog[i]:
            answer += "w"
        elif numLog[i+1] + 1 == numLog[i]:
            answer += "s"
        elif numLog[i+1] - 10 == numLog[i]:
            answer += "d"
        else:
            answer += "a"
        
    return answer

# -------------- 다른풀이 -----------------
# def solution(log):
#     res=''
#     joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
#     print(joystick)
#     for i in range(1,len(log)):
#         res+=joystick[log[i]-log[i-1]]
#     return res