# https://www.acmicpc.net/problem/2439

from sys import stdin

n = int(stdin.readline())
for i in range(1, n + 1):
    print(f'{" " * (n - i)}{"*" * i}')
