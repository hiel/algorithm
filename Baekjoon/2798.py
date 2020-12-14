# https://www.acmicpc.net/problem/2798

from sys import stdin

n, m = map(int, stdin.readline().rstrip().split(' '))
c = list(map(int, stdin.readline().rstrip().split(' ')))

mx = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            s = c[i] + c[j] + c[k]
            if s <= m:
                mx = max(mx, s)

print(mx)
