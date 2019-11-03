# https://programmers.co.kr/learn/courses/30/lessons/42889

import operator


def solution(N, stages):
    answer = []
    temp = []
    for i in range(N+1):
        temp.append(0)
        for user in stages:
            if i+1 <= user:
                temp[i] += 1
    
    temp2 = {}
    for i in range(N):
        if temp[i] == 0:
            temp2[i+1] = 0
        else:
            temp2[i+1] = 1 - temp[i+1] / temp[i]

    temp2 = sorted(temp2.items(), key=operator.itemgetter(1), reverse=True)
    for t in temp2:
        v, k = t
        answer.append(v)

    return answer


n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))

n = 4
stages = [4,4,4,4,4]
print(solution(n, stages))
