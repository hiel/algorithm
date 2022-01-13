# https://www.acmicpc.net/problem/2869

import math
from sys import stdin

a, b, v = map(int, stdin.readline().rstrip().split(' '))

d = 1
v -= a

d += math.ceil(v / (a - b))

print(d)
