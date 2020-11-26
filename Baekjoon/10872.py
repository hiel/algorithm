# https://www.acmicpc.net/problem/10872

from sys import stdin

s = 1
for i in range(int(stdin.readline().rstrip())):
    s *= i+1
print(s)
