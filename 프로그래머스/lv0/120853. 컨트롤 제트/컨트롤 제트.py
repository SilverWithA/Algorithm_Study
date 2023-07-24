def solution(s):
    
    # 공백을 기준으로 문자열을 나눠 answer 변수에 저장
    answer = s.split(" ")
    # 리스트 형으로 담김
    # print(answer)
    
    result =[]
    for i in range(len(answer)):
        if answer[i] != 'Z':
            result.append(int(answer[i]))
        else:
            result.pop()
            
    return sum(result)
    
    