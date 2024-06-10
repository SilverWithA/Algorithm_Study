N, K = map(int, input().split())


a = 1
b = 1
for i in range(N-K+1, N+1):
    a *= i

for j in range(1, K+1):
    b *= j

print(int(a/b))