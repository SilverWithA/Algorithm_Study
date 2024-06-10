n, max_value = map(int, input().split())
cards = list(map(int, input().split()))

# 3개의 숫자 선택
res = []
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            if cards[i] + cards[j] + cards[k] > max_value:
                continue
            res.append(cards[i] + cards[j] + cards[k])

print(max(res))
