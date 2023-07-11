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