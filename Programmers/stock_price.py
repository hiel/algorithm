# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

## 1
## 테스트 1 〉	통과 (123.39ms, 142MB)
## 테스트 2 〉	통과 (95.80ms, 105MB)
## 테스트 3 〉	통과 (157.04ms, 156MB)
## 테스트 4 〉	통과 (109.85ms, 120MB)
## 테스트 5 〉	통과 (77.59ms, 88.2MB)
def solution(prices):
    answer = []

    for i in range(len(prices)):
        v = 0
        for j in range(i+1, len(prices)):
            v += 1
            if prices[i] > prices[j]:
                break

        answer.append(v)

    return answer

## 2
## 테스트 1 〉	통과 (140.67ms, 141MB)
## 테스트 2 〉	통과 (115.93ms, 105MB)
## 테스트 3 〉	통과 (192.36ms, 158MB)
## 테스트 4 〉	통과 (140.09ms, 122MB)
## 테스트 5 〉	통과 (84.34ms, 87.5MB)
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer

# 이것과 완전히 동일한 코드인데 range()가 아닌 enumerate()를 사용했을 때는 왜 효율성 테스트에서 시간초과가 발생하는걸까요? 정말 미스테리합니다...
# enumerate()는 반복 자료형 내 원소를 하나씩 다 봐야하니까 O(n) 인 반면, range()는 O(1)인 걸로 알고 있습니다.
