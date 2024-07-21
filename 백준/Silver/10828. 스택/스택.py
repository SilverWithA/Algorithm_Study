import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    command = sys.stdin.readline()

    if 'push' in command:
        command, num = command.split()
        stack.append(int(num))

    if 'pop' in command:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    if 'size' in command:
        print(len(stack))

    if 'empty' in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if 'top' in command:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

