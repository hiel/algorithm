# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

# 타입별로 경우의 수를 다 곱함
# 해당 타입을 입지 않는 경우도 있으므로 경우의 수에 +1 이 필요
# 마지막으로, 모두 입지 않는 경우는 없으므로 +1
def solution(clothes):
    answer = 1

    m_dict = {}
    for cloth in clothes:
        c_type = cloth[1]
        if c_type not in m_dict:
            m_dict[c_type] = 0

        m_dict[c_type] += 1

    for m_d in m_dict.values():
        answer *= m_d + 1

    return answer - 1

print(solution([['A', 'X'], ['B', 'X'], ['C', 'X'], ['D', 'Y'], ['E', 'Y'], ['F', 'Z']]))
