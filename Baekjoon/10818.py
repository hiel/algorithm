# https://www.acmicpc.net/problem/10818

from sys import stdin

stdin.readline()
a = list(map(int, stdin.readline().rstrip().split(' ')))
print(str(min(a)) + ' ' + str(max(a)))
