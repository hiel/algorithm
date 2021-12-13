# https://www.acmicpc.net/problem/1546

from sys import stdin

s = m = 0
n = int(stdin.readline().rstrip())
for e in stdin.readline().rstrip().split(' '):
    m = max(m, int(e))
    s += int(e)

print(s / m * 100 / n)
