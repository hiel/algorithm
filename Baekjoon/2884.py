# https://www.acmicpc.net/problem/2884

from sys import stdin

h, m = list(map(int, stdin.readline().rstrip().split(' ')))

m -= 45
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24

print(h, m)
