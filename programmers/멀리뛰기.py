# 프로그래머스 - 멀리뛰기
# URL : https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3

def solution(n):
    answer = 0
    dpList = [0] * 2001
    dpList[1] = 1
    dpList[2] = 2

    for i in range(3, n+1):
        dpList[i] = (dpList[i-2] + dpList[i-1]) % 1234567

    answer = dpList[n]
    return answer
