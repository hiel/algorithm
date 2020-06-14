# 탑
# https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    answer = [0] * len(heights)

    for i, height in enumerate(heights):
        for j in reversed(range(i)):
            if height < heights[j]:
                answer[i] = j+1
                break

    return answer

# range로 enumerate를 대체
# range의 step을 -1로 설정해 reversed를 대체
# def solution(h):
#     ans = [0] * len(h)
#     for i in range(len(h)-1, 0, -1):
#         for j in range(i-1, -1, -1):
#             if h[i] < h[j]:
#                 ans[i] = j+1
#                 break
#     return ans

print(solution([6,9,5,7,4])) # answer == [0,0,2,2,4]
