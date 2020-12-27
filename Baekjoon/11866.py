# https://www.acmicpc.net/problem/11866

from sys import stdin

n, k = map(int, stdin.readline().rstrip().split(' '))
q = list(range(1, n+1))
r = []

while len(q) > 0:
    for _ in range(k-1):
        q.append(q.pop(0))
    r.append(str(q.pop(0)))

print('<' + ', '.join(r) + '>')
