# https://www.acmicpc.net/problem/10870

from sys import stdin

n = int(stdin.readline())

if n <= 1:
    print(n)
else:
    ary = [0, 1]
    for i in range(2, n+1):
        ary.append(ary[i-1] + ary[i-2])
    print(ary[n])
