# https://www.acmicpc.net/problem/11382

from sys import stdin


[a, b, c] = map(lambda e: int(e), stdin.readline().split(" "))
print(a + b + c)