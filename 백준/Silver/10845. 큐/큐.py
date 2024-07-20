import sys
n = int(sys.stdin.readline())
q = []
for _ in range(n):
    command = str(sys.stdin.readline())

    if 'push' in command:
        command, num = command.split()
        q.append(int(num))

    if 'front' in command:
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    if 'back' in command:
        if len(q) > 0:
            print(q[-1])  
        else:
            print(-1)

    if 'pop' in command:
        if len(q) > 0:
            print(q.pop(0))
        else:
            print(-1)

    if 'size' in command:
        print(len(q))

    if 'empty' in command:
        if len(q) == 0:
            print(1)
        else:
            print(0)
