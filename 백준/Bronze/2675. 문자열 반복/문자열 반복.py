n = int(input())
list = []
for _ in range(n):
    cnt, s = input().split(' ')
    list.append([int(cnt), s])


for cnt, s in list:
    answer = ''
    for char in s:
        answer += (char * cnt)
    print(answer)