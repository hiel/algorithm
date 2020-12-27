# https://www.acmicpc.net/problem/11022

from sys import stdin

for i in range(1, int(stdin.readline()) + 1):
    a, b = map(int, stdin.readline().rstrip().split(' '))
    print(f'Case #{i}: {a} + {b} = {a + b}')
