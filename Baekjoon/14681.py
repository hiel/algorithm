# https://www.acmicpc.net/problem/14681

a = int(input())
b = int(input())
print((1 if b > 0 else 4) if a > 0 else (2 if b > 0 else 3))
