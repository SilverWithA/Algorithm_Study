answer = 0
for _ in range(int(input())):
    tmp = ''
    for char in input():
        if char not in tmp:
            tmp += char

        elif char != tmp[-1:]:
            break
    else:
        answer += 1

print(answer)