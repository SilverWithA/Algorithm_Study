# 데이터 받아오기
n = int(input())


line = list(map(int, input().split()))


# print("정렬 전: ", line)
line.sort()
# print"정렬 후: ",line)

result = [0] * len(line)

for i in range(len(line)):
    result[i] = sum(line[:i+1])

print(sum(result))