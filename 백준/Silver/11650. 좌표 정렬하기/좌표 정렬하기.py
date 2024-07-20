import sys

n = int(sys.stdin.readline())

coordin = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coordin.append([x,y])

coordin.sort(key = lambda x: (x[0], x[1]))


for x ,y in coordin:
    print(x, y)
