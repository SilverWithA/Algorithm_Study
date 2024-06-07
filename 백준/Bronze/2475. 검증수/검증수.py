unique_nums = map(int, input().split())


sum = 0
for num in unique_nums:
    sum += num * num


print(sum % 10)
