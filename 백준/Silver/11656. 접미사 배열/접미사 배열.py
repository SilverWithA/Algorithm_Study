s = input()

suffix = []
for i in range(len(s)):
    suffix.append(s[i:])

suffix.sort()
for suff in suffix:
    print(suff)