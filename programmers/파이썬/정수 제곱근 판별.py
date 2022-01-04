def solution(n):
    answer = 0
    squrts = int(n ** 0.5)

    if squrts ** 2 == n:
        answer = (squrts + 1) ** 2
    else:
        answer = -1


    return answer
