# https://www.acmicpc.net/problem/1152

from sys import stdin

l = stdin.readline().strip().split(' ')
try:
    l.remove('')
except Exception:
    pass
print(len(l))
