# https://www.acmicpc.net/problem/25304

from sys import stdin


x = int(stdin.readline())
n = int(stdin.readline())
ps = []
for _ in range(n):
    ps.append(map(lambda e: int(e), stdin.readline().split(" ")))

for p, s in ps:
    x -= p * s

print('Yes' if x == 0 else 'No')