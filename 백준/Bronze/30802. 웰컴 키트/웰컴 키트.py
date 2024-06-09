
n = int(input())
sizes = map(int, input().split())
T, P = map(int, input().split())


T_bundle = 0
for size in sizes:
    if size % T != 0:
        T_bundle += ((int(size / T))+1)
    else:
        T_bundle += (int(size / T))

print(T_bundle)
print(int(n / P), n % P)