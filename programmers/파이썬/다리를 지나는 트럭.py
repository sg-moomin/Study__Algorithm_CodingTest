from collections import deque

def solution(bridge_length, weight, truck_weights):

    bride = [0] * bridge_length
    count = 0
    maxSize = 0
    while len(bride) > 0:
        count += 1
        maxText = bride.pop(0)
        if maxText != 0:
            maxSize -= maxText
        if len(truck_weights) != 0:
            if maxSize + truck_weights[0] <= weight:
                tmp = truck_weights.pop(0)
                maxSize += tmp
                bride.append(tmp)
            else:
                bride.append(0)



    return count
