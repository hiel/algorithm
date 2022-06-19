# https://www.acmicpc.net/problem/2839

from sys import stdin

r = 0
n = int(stdin.readline())

while True:
    if n % 5 == 0:
        r += int(n / 5)
        break

    n -= 3
    r += 1

    if n == 0:
        break
    if n < 0:
        r = -1
        break

print(r)
