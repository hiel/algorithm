# https://www.acmicpc.net/problem/1436

from sys import stdin

n = int(stdin.readline())

t = 666
while True:
    if '666' in str(t):
        n -= 1
        if n == 0:
            print(t)
            break
    t += 1
