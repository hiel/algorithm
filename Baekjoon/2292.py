# https://www.acmicpc.net/problem/2292

from sys import stdin

n = int(stdin.readline())
r = 0
t = 1
while True:
    t += 6 * r
    if t >= n:
        print(r + 1)
        break
    r += 1
