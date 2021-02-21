from collections import deque
def solution(prices):
# 1번 풀이 시간초과
#     stacks = deque(prices)
#     result = []
#     temp = 0
#     count = 0
#     inputprice = 0
#     numbers = 0
#     while len(stacks) > 0:
#         if inputprice == 0:
#             numbers = 0
#             inputprice = stacks.popleft()

#         else:
#             if stacks[numbers] >= inputprice:
#                 count += 1
#                 numbers += 1
#             else:
#                 result.append(count + 1)
#                 inputprice = 0
#                 numbers = 0
#                 count = 0

#             if numbers == len(stacks):
#                 result.append(count)
#                 numbers = 0
#                 inputprice = 0
#                 count = 0

#         if len(stacks) == 0:
#             result.append(0)
#             break

#     return result

    result = [0] * len(prices)
    for i in range(len(prices)):
        count = 1
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                result[i] += count
            else:
                result[i] += count
                break

    return result
