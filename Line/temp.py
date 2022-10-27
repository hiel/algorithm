import sys

line = sys.stdin.readline().split(' ')
nums = list(map(int, line))
length = len(nums)
if length == 1:
    if nums[0] < -200 or nums[0] > 200:
        print("ERROR")
    else:
        print(nums[0])
    exit(0)
results = []

for i, n in enumerate(nums):
    if n < -200 or n > 200:
        continue

    if i > 1 and abs(n - nums[i-2]) < 3:
        results.append(n)
        continue
    if i > 0 and abs(n - nums[i-1]) < 3:
        results.append(n)
        continue
    if i+1 < length and abs(n - nums[i+1]) < 3:
        results.append(n)
        continue
    if i+2 < length and abs(n - nums[i+2]) < 3:
        results.append(n)
        continue

if len(results) == 0:
    print("ERROR")
else:
    print(int(sum(results) / len(results)))
