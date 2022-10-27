def solution(s):
    answer = 0

    for i, c1 in enumerate(s):
        if c1 not in ['a', 'z']:
            continue
        for c2 in s[i+1:]:
            if c2 in ['a', 'z']:
                if c1 != c2:
                    answer += 1
                break

    return answer

print(solution('abcz'))
print(solution('zabzczxa'))
print(solution('abcd'))
