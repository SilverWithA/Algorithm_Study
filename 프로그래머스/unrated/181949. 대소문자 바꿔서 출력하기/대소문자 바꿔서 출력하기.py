str = input()


# 문자열 요소를 리스트 요소로 변환
str = list(str)
# print(str)   # ['a', 'B', 'c', 'D', 'e', 'F', 'g']

for i in range(len(str)):
    if str[i].islower():
        str[i] = str[i].upper()
    else:
         str[i] = str[i].lower()
            
print("".join(str))
        
