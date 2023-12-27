n = int(input())
s = input()
s = s.replace('pPAp', '')
print(int((n - len(s))/4))