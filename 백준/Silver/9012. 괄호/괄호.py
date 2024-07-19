import sys

n = int(sys.stdin.readline())
for _ in range(n):
    tmp = sys.stdin.readline()
    cnt = 0
    bnt = True
    for t in list(tmp):
        if t == "(":
            cnt += 1
        elif t == ")":
            if cnt > 0:
                cnt -= 1
            else:
                bnt = False
                break

    if cnt == 0 and bnt:
        print("YES")
    else:
        print("NO")


