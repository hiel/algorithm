def solution(v):
    return [v[0][0] ^ v[1][0] ^ v[2][0], v[0][1] ^ v[1][1] ^ v[2][1]]


print(solution([[1,4], [3,4], [3,10]]))
