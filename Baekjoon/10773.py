# https://www.acmicpc.net/problem/10773

from sys import stdin

s = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n == 0:
        s.pop()
    else:
        s.append(n)
print(sum(s))
