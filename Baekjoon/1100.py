# https://www.acmicpc.net/problem/1100

from sys import stdin

r = 0
for i in range(8):
    t = stdin.readline().rstrip()
    for j in range(8):
        if t[j] == 'F' and (i+j) % 2 == 0:
            r += 1
print(r)
