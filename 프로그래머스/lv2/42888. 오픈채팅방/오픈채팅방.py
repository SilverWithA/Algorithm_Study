def solution(record):
    
    # 해시 딕셔너리로 풀어보기
    # record들을 list로 만들어서 단어별로 인덱싱이 편하도록 만들기
    uid = {}
    
    for i in range(len(record)):
        # split()을 사용하면 공백 기준으로 문자열을 리스트로 만들어준다
        record[i] = record[i].split()
    # print(record)
    
    # 딕셔너리에 key값은 uid값을 value 값은 닉네임 상태를 넣기
    for j in range(len(record)):
        if record[j][0] == 'Enter':  
            uid[record[j][1]] = [record[j][2]]
    

    
    # 완전탐색으로 record의 각 요소의 첫번째 요소가 "change"이면 uid에 해당하는 바뀐 닉네임에 저장
    for i in range(len(record)):
        if record[i][0] == 'Change':
            uid[record[i][1]].append(record[i][2])
        if record[i][0] == 'Enter' and record[i][1] in uid:
            uid[record[i][1]].append(record[i][2])
    # return할때 각 uiid에 있는 마지막 닉네임만 출력하면 됨
    answer = []
    for i in range(len(record)):
        temp = ''
        if record[i][0] == "Enter":
            temp += uid[record[i][1]][-1] + "님이 들어왔습니다."
            
        elif record[i][0] == "Leave":
            temp += uid[record[i][1]][-1] + "님이 나갔습니다."
        else:
            continue
        answer.append(temp)
            
    return answer
            
        