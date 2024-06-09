
n = int(input())
total = 1
i = 0
while True:
    total += (6 * i)

    if n <= total:
        print(i+1)
        break
    i += 1
