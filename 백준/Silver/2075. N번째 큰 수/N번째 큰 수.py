import heapq

n = int(input())
arr = []
pq = []
for i in range(n):
    # 입력값 모두 한 리스트에 모으기
    temp = list(map(int, input().split()))
    for num in temp:

        # 현재 pq의 크기가 n보다 작으면
        if len(pq) < n:
            heapq.heappush(pq, num)

        else:
            temp_min = heapq.heappop(pq)
            if temp_min < num:
                heapq.heappush(pq, num)
            else:
                heapq.heappush(pq, temp_min)


print(heapq.heappop(pq))