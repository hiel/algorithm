# https://www.acmicpc.net/problem/2231

from sys import stdin

n = int(stdin.readline())

i = 1
while i != 1000000:
    s = i
    for c in str(i):
        s += int(c)
    if s == n:
        print(i)
        exit(0)
    i += 1
print(0)
