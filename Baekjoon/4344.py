# https://www.acmicpc.net/problem/4344

from sys import stdin

l = []
for _ in range(int(stdin.readline().rstrip())):
    l.append(list(map(int, stdin.readline().rstrip().split(' '))))

for i in l:
    avg = sum(i[1:]) / i[0]
    print('%.3f' % round(((len([e for e in i[1:] if e > avg]) / i[0]) * 100), 3) + '%')
