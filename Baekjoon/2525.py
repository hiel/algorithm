# https://www.acmicpc.net/problem/2525

import math
from sys import stdin


[h, m] = map(lambda e: int(e), stdin.readline().split(" "))
cook = int(stdin.readline())

h = (h + math.floor((m + cook) / 60)) % 24
m = (m + cook) % 60
print(f'{h} {m}')