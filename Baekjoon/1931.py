# https://www.acmicpc.net/problem/1931

import sys

meetings = []
for _ in range(int(sys.stdin.readline())):
    start, end = sys.stdin.readline().rstrip().split(' ')
    meetings.append((int(start), int(end)))

meetings.sort(key=lambda m: (m[1], m[0]))

result = 1
temp = meetings[0]
for meeting in meetings[1:]:
    if meeting[0] >= temp[1]:
        result += 1
        temp = meeting
        continue

print(result)
