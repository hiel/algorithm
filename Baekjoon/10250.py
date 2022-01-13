# https://www.acmicpc.net/problem/10250

import math
from sys import stdin

for _ in range(int(stdin.readline())):
    h, w, n = map(int, stdin.readline().rstrip().split(' '))
    print(str(n % h if n % h != 0 else h) + str(math.ceil(n / h)).zfill(2))
