
# 입력부
n = int(input())    # 숫자의 개수
nums = map(int, input().split())    # 숫자들

isNotPrime = 0
for num in nums:
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                isNotPrime += 1
                break

    if num == 1:
        isNotPrime += 1
print(n-isNotPrime)