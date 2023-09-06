def solution(name, yearning, photo):
    
    hash = {}
    result = []
    
    for i in range(len(name)):
        hash[name[i]] = yearning[i]
        
    for i in range(len(photo)):
        cnt = 0
        for person in photo[i]:
            if person in hash:
                cnt += hash[person]
            else:
                continue
        result.append(cnt)

                  
    return result