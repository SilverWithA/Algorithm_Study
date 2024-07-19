# 부녀회장

apartment = [[1] for _ in range(15)]
apartment[0] = [i for i in range(1, 15)]
# print(apartment)

case = int(input())

# k층 , n호

# 재귀로 풀기
def calculate_host(k, n):
    # print("k, n: ", k, n)

    if len(apartment[k - 1]) < n:   # k-1층에 n호까지만큼 거주민수가 계산이 되지 않았다면
        calculate_host(k - 1, n)    # k-1층에 n호까지 거주민수 계산


    for i in range(len(apartment[k]), n): # 현재 계산이 된 호수부터 n까지
        # print("i: ", i)
        # print(apartment[k - 1][i])
        apartment[k].append(apartment[k - 1][i] + apartment[k][i - 1])


res = []
for i in range(case):
    k = int(input())  # 층수
    n = int(input())  # 호수

    calculate_host(k, n)
    res.append(apartment[k][n-1])
    # print("apartment: ", apartment)


for re in res:
    print(re)
