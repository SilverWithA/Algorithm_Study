n = int(input())
#
t = 1
for i in range(1, n + 1):
    t *= i

s = str(t)

cnt = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == "0":
        cnt += 1
    else:
        print(cnt)
        break
