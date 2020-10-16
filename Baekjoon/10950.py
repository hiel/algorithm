# https://www.acmicpc.net/problem/10950

ary = []
for _ in range(int(input())):
    a, b = input().split(' ')
    ary.append(int(a) + int(b))

for i in ary:
    print(i)
