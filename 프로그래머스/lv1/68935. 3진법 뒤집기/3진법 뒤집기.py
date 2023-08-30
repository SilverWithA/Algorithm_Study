def solution(n):    
    
    trit = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        trit += str(mod)
    return int(trit,3)
    



