def solution(s):
    s = s.lower()
    res = s.split(" ")
    for i in range(len(res)):
        res[i] = res[i][:1].upper()+res[i][1:]
        
    return ' '.join(res)
        
    
