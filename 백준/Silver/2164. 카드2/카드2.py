# 시간 초과
import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([i for i in range(1, n+1)])


step = 0
while(len(q) > 1):
    if step % 2 == 0:
        q.popleft()
    else:
        q.append(q.popleft())
    step += 1
print(q.popleft())