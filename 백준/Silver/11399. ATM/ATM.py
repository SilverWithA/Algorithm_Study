import sys
customer = int(sys.stdin.readline())

line = list(map(int, sys.stdin.readline().split(' ')))
line.sort()

res = 0
for i, time in enumerate(line):
    res += time * (len(line) - i)
print(res)
