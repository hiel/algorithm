# https://www.acmicpc.net/problem/2581

from sys import stdin

min = None
s = 0

m = int(stdin.readline())
n = int(stdin.readline())


def __is_prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    return is_prime


for i in range(m, n+1):
    if i > 1 and __is_prime(i) is True:
        if min is None:
            min = i
        s += i

print(-1 if min is None else f'{s}\n{min}')
