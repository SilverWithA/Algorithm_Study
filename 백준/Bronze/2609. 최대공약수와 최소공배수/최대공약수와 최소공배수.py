import sys

# 입력받는 방법 주의 - map 사용 유무 차이
a, b = map(int, sys.stdin.readline().split())

if b < a:
    a, b = b, a

# 약수 찾기
a_tmp = []
b_tmp = []
for i in range(b + 1,0,-1):
    if a % i == 0 and i <=a:
        a_tmp.append(i)
    if b % i == 0:
        b_tmp.append(i)

for tmp in b_tmp:
    if tmp in a_tmp:
        print(tmp)
        break


a2_tmp = []
b2_tmp = []
# 배수 찾기
i = 0
while (i <= b):
    i += 1
    a2_tmp.append(a * i)
    b2_tmp.append(b * i)

for tmp in b2_tmp:
    if tmp in a2_tmp:
        print(tmp)
        break