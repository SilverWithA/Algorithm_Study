def solution(babbling):
    babys = ["aya", "ye", "woo", "ma"]
    cnt = 0 
    
    for i in range(len(babbling)):
        for j in babys:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j,"1")
                
    for i in range(len(babbling)):
        if babbling[i].isdigit():
            cnt += 1
            
    return cnt
        

            
    # print(babbling)
            
    # try:
    #     int(babbling)
    #     cnt +=1
    # except: print("에러발생")