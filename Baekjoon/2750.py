# https://www.acmicpc.net/problem/2750

from sys import stdin

a = []
for _ in range(int(stdin.readline())):
    a.append(int(stdin.readline()))
a = sorted(a)
[print(b) for b in a]
