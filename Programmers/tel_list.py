# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

# 0.18ms
def solution(phone_book):
    length = len(phone_book)
    for i, phone in enumerate(phone_book):
        for j in range(i+1, length):
            phone2 = phone_book[j]
            if phone == phone2[:len(phone)] or phone[:len(phone2)] == phone2:
                return False

    return True

# 0.12ms
def solution(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True
