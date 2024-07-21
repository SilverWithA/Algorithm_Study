import sys

n = int(sys.stdin.readline())
S = set()

for _ in range(n):
    command = sys.stdin.readline()
    if 'all' in command:
        S = set(i for i in range(1, 21))
        continue
    if 'empty' in command:
        S = set()
        continue

    command, x = command.split()
    x = int(x)

    if 'add' in command:
        S.add(x)

    if 'remove' in command:
        if x in S:
            S.remove(x)

    if 'check' in command:
        if x in S:
            print(1)
        else:
            print(0)

    if 'toggle' in command:
        if x in S:
            S.remove(x)
        else:
            S.add(x)


