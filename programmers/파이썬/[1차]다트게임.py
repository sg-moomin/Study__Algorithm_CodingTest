# 프로그래머스 : [1차] 다트 게임
# URL : https://programmers.co.kr/learn/courses/30/lessons/17682

import math

def solution(dartResult):
    darts = []
    starsNum = []
    result = [0] * 3
    dartStr = ""
    chks = ""
    rDartResult = ""

    rDartResult = dartResult + "K"

    for i in range(len(rDartResult)):
        if rDartResult[i] == "S" or rDartResult[i] == "D" or rDartResult[i] == "T" or rDartResult[i] == "K":
            darts.append(dartStr + rDartResult[i])
            dartStr = ""
        else:
            dartStr += rDartResult[i]

    for i in range(len(darts)):
        chks = ""
        for j in darts[i]:
            if j == "S":
                result[i] = int(chks)
                result[i] = int(math.pow(result[i], 1))
            elif j == "D":
                result[i] = int(chks)
                result[i] = int(math.pow(result[i], 2))
            elif j == "T":
                result[i] = int(chks)
                result[i] = int(math.pow(result[i], 3))
            elif j == "#" or j == "*":
                if j == "#":
                    result[i-1] *= (-1)
                else:
                    result[i-1] *= 2
                    result[i-2] *= 2
            else:
                chks += j

    return sum(result)
