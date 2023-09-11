def solution(s1, s2):
    result = 0
    if len(s1) > len(s2):
        s1, s2 = s2, s1
        
    for i in s1:
        if i in s2:
            result +=1

    return result