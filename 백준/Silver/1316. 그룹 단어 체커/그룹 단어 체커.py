n = int(input())
arr = []
for cnt in range(n):
    arr.append(input())

answer = 0

for word in arr:
    tmep = []
    tmep.append(word[0])
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            tmep.append(word[j+1])

    if len(tmep) == len(list(set(tmep))):
        answer += 1

print(answer)