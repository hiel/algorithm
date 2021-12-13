# https://www.acmicpc.net/problem/8958

from sys import stdin

for _ in range(int(stdin.readline())):
    s = 0
    t = 0
    for c in stdin.readline():
        if c == 'O':
            s += 1 + t
            t += 1
        else:
            t = 0
    print(s)
