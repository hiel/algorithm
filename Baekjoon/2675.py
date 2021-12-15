# https://www.acmicpc.net/problem/2675

from sys import stdin

for _ in range(int(stdin.readline())):
    r, s = stdin.readline().rstrip().split(' ')
    p = ''
    for c in s:
        p += c*int(r)
    print(p)
