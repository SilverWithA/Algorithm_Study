import sys

n, k = map(int, sys.stdin.readline().split())
queue = [i for i in range(1, n + 1)]
# print(queue)
res = []

step = 1
while (len(queue) != 0):
    if step == k:
        res.append(queue.pop(0))
        step = 1
    else:
        queue.append(queue.pop(0))
        step += 1
print("<", end='')
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end='')
    else:
        print(res[i], end=', ')

print(">", end='')