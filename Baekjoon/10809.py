# https://www.acmicpc.net/problem/10809

from sys import stdin

s = stdin.readline().rstrip()
a = [-1]*26

for i in range(len(s)):
    if a[ord(s[i])-97] == -1:
        a[ord(s[i])-97] = i

print(' '.join(map(str, a)))
