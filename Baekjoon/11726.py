# https://www.acmicpc.net/problem/11726

import math
from sys import stdin


n = int(stdin.readline())

r = 1
for _ in range(1, math.floor(n / 2) + 1):
    r *= 2

print(r)

if n % 2 == 1:
    r *= math.ceil(n / 2)

print(r)

# ** ** ** **