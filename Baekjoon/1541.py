# https://www.acmicpc.net/problem/1541

from sys import stdin

r = 0
i = stdin.readline().rstrip().split('-')

for ii in i[1:]:
    for iii in ii.split('+'):
        r -= int(iii)

for ii in i[0].split('+'):
    r += int(ii)

print(r)
