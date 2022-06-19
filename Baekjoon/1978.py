# https://www.acmicpc.net/problem/1978

from sys import stdin

r = 0

stdin.readline()


def __is_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    return is_prime


for i in map(int, stdin.readline().split()):
    if i > 1 and __is_prime(i) is True:
        r += 1

print(r)
