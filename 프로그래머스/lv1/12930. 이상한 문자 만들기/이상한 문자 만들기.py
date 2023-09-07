def solution(s):
    s = s.lower()
    words = s.split(' ')
    print(words)
    
    answer = []
    
    for word in words:
        temp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer.append(temp)
    print(answer)

#     result = ''
#     for i in range(len(answer)):
#         result += answer[i] + " "
                
#     return result[:-1]
    return ' '.join(answer)
                