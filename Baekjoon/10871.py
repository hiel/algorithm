# https://www.acmicpc.net/problem/10871

from sys import stdin

n, x = map(int, stdin.readline().rstrip().split(' '))
print(' '.join(map(str, filter(lambda i: i < x, map(int, stdin.readline().rstrip().split(' '))))))
