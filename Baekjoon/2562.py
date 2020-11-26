# https://www.acmicpc.net/problem/2562

from sys import stdin

result = 0
result_index = -1
for i in range(9):
    a = int(stdin.readline().rstrip())
    if a > result:
        result = a
        result_index = i

print(result)
print(result_index+1)
