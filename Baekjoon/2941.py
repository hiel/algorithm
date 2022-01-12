# https://www.acmicpc.net/problem/2941

from sys import stdin

s = stdin.readline().rstrip()
for p in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(p, '@')

print(len(s))
