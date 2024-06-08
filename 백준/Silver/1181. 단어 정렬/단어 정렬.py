n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append((len(s),s))


# list 중복 제거
strings = list(set(strings))
strings.sort(key= lambda x: (x[0], x[1]))




for length, string in strings:
    print(string)