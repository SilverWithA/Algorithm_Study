from collections import deque
m, n = map(int, input().split())
money = deque((map(int, input().split())))



sliding = deque()
max = 0
tmp_sum = 0
for i in range(m-n+1):
    while len(sliding) < n:
        t = money.popleft()
        tmp_sum += t
        sliding.append(t)

    if tmp_sum > max:
        max = tmp_sum

    tmp_sum -= sliding.popleft()

print(max)