def solution(n, control):
    n += control.count("w")     # 3
    n -= control.count("s")     # 4
    n += ( control.count("d") * 10 )  # 2 
    n -= ( control.count("a") * 10 ) # 2 
    return n