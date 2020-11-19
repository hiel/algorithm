# https://www.acmicpc.net/problem/15552

from sys import stdin

for _ in range(int(stdin.readline())):
    start, end = stdin.readline().rstrip().split(' ')
    print(int(start) + int(end))
