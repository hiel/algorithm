def solution(n, bankbook):
    print('#'*10) #
    print(n) #
    answer = 0

    bankbook = sorted(bankbook, reverse=True)
    for i, m in enumerate(bankbook):
        t = [m] #
        answer += 1
        s = m
        for m2 in bankbook[i+1:]:
            if s + m2 <= n:
                t.append(m2) #
                s += m2
                bankbook.remove(m2)
        print(t, sum(t))

    return answer

# print(solution(10, [8, 4, 2, 5, 3, 7]))
# print(solution(10, [1, 2, 3, 3, 3, 8]))
# print(solution(10, [1, 2, 3, 4, 5, 6]))
# print(solution(10, [10, 10]))
print(solution(5, [1, 1, 1]))
