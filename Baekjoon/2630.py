# https://www.acmicpc.net/problem/2630

from sys import stdin

a = []
n = int(stdin.readline())
for _ in range(n):
    a.append(stdin.readline().rstrip().split(' '))

r0 = r1 = 0
def rec(x, y, length):
    global r0, r1
    t = a[x][y]
    for i in range(length):
        for j in range(length):
            if t != a[x+i][y+j]:
                l = int(length/2)
                rec(x, y, l)
                rec(x+l, y, l)
                rec(x, y+l, l)
                rec(x+l, y, l)
                return
            else:
                t = a[x+i][y+j]
    if t == '0':
        r0 += 1
    else:
        r1 += 1
rec(0, 0, n)
print(r0)
print(r1)
