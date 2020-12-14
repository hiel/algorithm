# https://www.acmicpc.net/problem/10828

from sys import stdin

stack = []
for _ in range(int(stdin.readline().rstrip())):
    command_ary = stdin.readline().rstrip().split(' ')
    command = command_ary[0]

    if command == 'push':
        stack.append(command_ary[1])
    elif command == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif command == 'top':
        print(stack[-1] if len(stack) > 0 else -1)
