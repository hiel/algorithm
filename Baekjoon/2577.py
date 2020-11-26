# https://www.acmicpc.net/problem/2577

from sys import stdin

s = 1
for _ in range(3):
    s *= int(stdin.readline().rstrip())

s = str(s)
for i in range(10):
    print(s.count(str(i)))
