# 정답코드
def solution(n):
    answer = 0

    for i in range(1, n+1):

        if n % i == 0:
            answer += i
        else:
            continue
    return answer

# 1번 2번 테스트 코드 실패
import math
def solution(n):
    temp = math.ceil(n ** 0.5)
    answer = 0

    for i in range(1, temp):
        if n % i == 0:
            answer += i + int(n / i)

    return answer
