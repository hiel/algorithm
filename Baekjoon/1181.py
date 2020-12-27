# https://www.acmicpc.net/problem/1181

from sys import stdin

t = []
for _ in range(int(stdin.readline())):
    t.append(stdin.readline().rstrip())

tp = None
for e in sorted(t, key=lambda e: (len(e), str.lower(e))):
    if tp != e:
        print(e)
        tp = e
