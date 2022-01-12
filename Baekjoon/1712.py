# https://www.acmicpc.net/problem/1712

from sys import stdin

a = list(map(int, stdin.readline().split(' ')))
try:
    print(max(int(a[0] / (a[2] - a[1]) + 1), -1))
except ZeroDivisionError:
    print(-1)
