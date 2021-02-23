def solution(number, k):

#     count = len(number) - k
#     numberCount = 0
#     index = 0
#     start = 0
#     result = ""
#     for i in range(count):
#         maxSize = number[start]
#         index = start
#         for j in range(start, i + k):
#             if maxSize < number[j]:
#                 maxSize = number[j]
#                 index = j

#         start = index + 1
#         result += maxSize



#     return result
#     startPoint, endPoint = number[0], 0
#     result = ""
#     for i in range(1, len(number)):
#         endPoint = number[i]
#         maxSize = ""
#         maxSize = max(startPoint, endPoint)
#         if maxSize != startPoint:
#             result += maxSize

#     if result == (len(number) - k):
#         return result
#     else:
#         if len(result) > (len(number) - k):
#             tmp = len(result) - (len(number) - k)
#             result = result[tmp:]
#             return result
#         else:
#             tmp = (len(number)- k) - len(result)
#             print(result, tmp)
#             result += number[:tmp]
#             return result
    startPoint, endPoint = number[0], 0
    result = ""
    textCase = number
    startPoint = textCase[0]
    textCase = textCase[1:]
    while len(textCase) != 0:
        endPoint = textCase[0]
        maxSize = max(endPoint, startPoint)
        if maxSize != startPoint:
            result += maxSize
            textCase = textCase[1:]

        else:
            startPoint = maxSize


    if len(result) == (len(number)- k):
        return result
    else:
        if len(result) > (len(number) - k):
            tmp = len(result) - (len(number) - k)
            result2 = result
            while tmp != 0:
                check = min(result2)
                i = result2.find(check)
                result = result2[:i] + result2[i+1:]
                tmp -= 1

            return result
        else:
            tmp = (len(number)- k) - len(result)
            result += number[:tmp]
            return result
