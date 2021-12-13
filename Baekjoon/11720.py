# https://www.acmicpc.net/problem/11720

from sys import stdin

n = int(stdin.readline())
a = stdin.readline().rstrip()

s = 0
for i in range(n):
    s += int(a[i])

print(s)
