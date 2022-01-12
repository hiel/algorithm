# https://www.acmicpc.net/problem/1316

from sys import stdin

r = i = int(stdin.readline())
for _ in range(i):
    t = ''
    ar = []
    for c in stdin.readline().rstrip():
        if c != t:
            if c in ar:
                r -= 1
                break
            t = c
            ar.append(c)
print(r)
