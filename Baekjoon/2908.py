# https://www.acmicpc.net/problem/2908

from sys import stdin

a = stdin.readline()

if int(a[0:3][::-1]) > int(a[4:7][::-1]):
    print(a[0:3][::-1])
else:
    print(a[4:7][::-1])
