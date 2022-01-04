def solution(n, times):
    startPoint, endPoint = min(times), min(times) * n
    answer = min(times) * n
    midPoint = 0

    while startPoint <= endPoint:
        midPoint = (startPoint + endPoint) // 2
        check = 0
        for i in range(len(times)):
            check += midPoint // times[i]

            if check >= n:
                answer = midPoint
                endPoint = midPoint - 1
                break


        if check < n:
            startPoint = midPoint + 1

    return answer
