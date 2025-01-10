# https://www.acmicpc.net/problem/1929

import math
from sys import stdin


m, n = map(lambda e: int(e), stdin.readline().split(' '))

t = [0 for _ in range(n + 1)]
for i in range(2, math.floor(n / 2) + 1):
    if t[i] == 1:
        continue
    j = i + i
    while j <= n:
        t[j] = 1
        j = j + i

for i in range(m, n + 1):
    if i != 1 and t[i] == 0:
        print(i)