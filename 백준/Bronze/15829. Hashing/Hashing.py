n = int(input())
s = input()

chars = []
for i in range(n):
    chars.append(s[i])


H = 0
for i in range(n):
    H += ((ord(chars[i])-96) * (31**i))

print(H % 1234567891)