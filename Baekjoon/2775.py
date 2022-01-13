# https://www.acmicpc.net/problem/2775

from sys import stdin

for _ in range(int(stdin.readline())):
    k = int(stdin.readline())
    n = int(stdin.readline())

    a = [[e+1 for e in range(n)]]

    for i in range(k):
        ta = []
        t = 0
        for j in range(n):
            t += a[i][j]
            ta.append(t)
        a.append(ta)
    print(a[k][n-1])
