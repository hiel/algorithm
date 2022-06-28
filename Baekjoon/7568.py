# https://www.acmicpc.net/problem/7568

from sys import stdin

l = [list(map(int, stdin.readline().split(' '))) + [1] for _ in range(int(stdin.readline()))]

for e in l:
    for e2 in l:
        if e[0] < e2[0] and e[1] < e2[1]:
            e[2] += 1

print(' '.join([str(e[2]) for e in l]))
