# 프로그래머스 > 소수 찾기
# URL : https://programmers.co.kr/learn/courses/30/lessons/12921

import math

def solution(n):
    check = 0;
    result = [0] * (n+1);
    decimal = int(math.sqrt(n))

    for i in range(2, n+1):
        if result[i] == 0:
            for j in range(i*i, n+1, i):
                result[j] = 1

    result[0] = 1
    result[1] = 1

    return result.count(0)
    
