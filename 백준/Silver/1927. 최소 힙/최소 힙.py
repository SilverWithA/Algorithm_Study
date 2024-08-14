import heapq, sys

h = []

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)

