# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length

    while len(bridge) > 0:
        answer += 1
        bridge.pop(0)

        if len(truck_weights) > 0:
            if sum(bridge) + truck_weights[0] > weight:
                bridge.append(0)
            else:
                bridge.append(truck_weights.pop(0))

    return answer
