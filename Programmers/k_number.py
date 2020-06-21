# K번쨰 수
# https://programmers.co.kr/learn/courses/30/lessons/42748

# 1
def solution(array, commands):
    answer = []

    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])

    return answer

# 2
# list, map, lambda를 사용
# 소스가 간결해짐
# python 공부 해야함.....
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 3
# i,j,k로 한번에 정의해서 풀어냄
# python 공부 해야함.....
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
