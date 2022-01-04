# 1. While문 풀이 - 시간 초과
# import heapq
# def solution(scoville, k):
#     mixScov = 0
#     mixCount = 0
#     scoville.sort()
#     while len(scoville) > 1:
#         mixScov = scoville[0] + (scoville[1] * 2)
#         scoville = scoville[2:]
#         scoville.append(mixScov)
#         mixCount += 1
#         scoville.sort()
#         if scoville[0] >= k:
#             return mixCount

#     if scoville[0] < k:
#         return -1


import heapq
def solution(scoville, k):
    heapq.heapify(scoville)
    mixCount = 0

    while len(scoville) > 1:
        number1 = heapq.heappop(scoville)
        number2 = heapq.heappop(scoville)
        maxSize = number1 + (number2 * 2)
        heapq.heappush(scoville, maxSize)
        mixCount += 1

        if scoville[0] >= k:
            return mixCount


    if scoville[0] < k :
        return -1
