import math
def solution(brown, yellow):
    # sumColor = brown + yellow
    # SecondNum = int(math.sqrt(sumColor))
    # FristNum = int(sumColor / SecondNum)
    # answer = [FristNum, SecondNum]
    # answer.sort(reverse=True)
    # return answer

#     sumColor = brown + yellow
#     if sumColor == 0:
#         return 0
#     result = []
#     for i in range(2, sumColor):
#         if sumColor % i == 0:
#             result.append(i)

#     anwser = []
#     midNum = len(result) // 2
#     for _ in range(len(result)):
#         if sumColor % result[midNum] == 0:
#             anwser.append([result[midNum], sumColor // result[midNum]])
#             break
#         else:
#             if sumColor % result[midNum - 1] == 0:
#                 anwser.append([result[midNum], sumColor // result[midNum - 1]])
#                 break
#             elif sumColor % result[midNum + 1] == 0:
#                 anwser.append([result[midNum], sumColor // result[midNum + 1]])
#                 break
#             else:
#                 midNum += 1

#     anwser.sort(reverse=True)
#     return anwser[0]

        sumColor = brown + yellow
        result = []


        for i in range(2, sumColor):
            if sumColor % i == 0:
                result.append(i)

        print(result)
        endPoint = -1
        answer = []
        for i in range(len(result)):
            if (result[i] - 2) * (result[endPoint] - 2) == yellow:
                answer.append([result[endPoint], result[i]])
                break
            else:
                endPoint = endPoint - 1


        return answer[0]
