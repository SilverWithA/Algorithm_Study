n1 = int(input())
arr1 = set(map(int,input().split()))
n2 = int(input())
arr2 = list(map(int,input().split()))

for num in arr2:
    print(1) if num in arr1 else print(0)