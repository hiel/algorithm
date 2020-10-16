# https://www.acmicpc.net/problem/1330

a = input()
b = input()

a1 = int(a[0]) * 100
a2 = int(a[1]) * 10
a3 = int(a[2])
b1 = int(b[0]) * 100
b2 = int(b[1]) * 10
b3 = int(b[2])

print(a1 * b3 + a2 * b3 + a3 * b3)
print(int((a1 * b2 + a2 * b2 + a3 * b2) / 10))
print(int((a1 * b1 + a2 * b1 + a3 * b1) / 100))
print(int(a) * int(b))
