from collections import defaultdict
n, m = map(int, input().split())

listed = defaultdict(int)

for _ in range(n+m):
    name = input()
    listed[name] += 1
    
res = []
for k, v in listed.items():
    if v > 1:
        res.append(k)
res.sort()

print(len(res))
for k in res:
    print(k)