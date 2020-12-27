# https://www.acmicpc.net/problem/2739

from sys import stdin

n = int(stdin.readline())
for i in list(range(1, 10)): print(f'{n} * {i} = {n * (i)}')
