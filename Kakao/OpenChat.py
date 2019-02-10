# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    dic = {}
    for r in record:
        if r[:1] != 'L':
            arr = r.split(' ')
            dic[arr[1]] = arr[2]
    
    answer = []
    for r in record:
        if r[:1] != 'C':
            arr = r.split(' ')
            name = dic[arr[1]]
            if r[:1] == 'E':
                answer.append(name + '님이 들어왔습니다.')
            elif r[:1] == 'L':
                answer.append(name + '님이 나갔습니다.')
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

solution(record)
