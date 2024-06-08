total = 1
for _ in range(3):
    num = int(input())
    total *= num


cnt = {}
for s in str(total):
    if s not in cnt:
        cnt[s] = 1
    else:
        cnt[s] += 1

for i in range(10):
    if str(i) not in cnt:
        print(0)
    else:
        print(cnt[str(i)])