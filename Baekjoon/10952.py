# https://www.acmicpc.net/problem/10952

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
