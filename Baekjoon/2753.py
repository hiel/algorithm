# https://www.acmicpc.net/problem/2753

a = int(input())

if a % 4 == 0:
    if a % 100 != 0 or a % 400 == 0:
        print(1)
        exit()

print(0)
