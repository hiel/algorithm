# https://www.acmicpc.net/problem/3003

from sys import stdin


n = list(map(lambda e: int(e), stdin.readline().split(" ")))
r = []
for i, e in enumerate([1, 1, 2, 2, 2, 8]):
    r.append(str(e - n[i]))
print(' '.join(r))