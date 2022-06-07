# N으로 표현
# url : https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(n, number):
    answer = -1
    dp = []

    if n == number:
        return 1

    for i in range(1, 9):
        arrs = set()
        unionStr = int(str(n) * i)
        arrs.add(unionStr)
        for j in range(0, i-1):
            for k in dp[j]:
                for z in dp[-j-1]:
                    arrs.add(k + z)
                    arrs.add(k - z)
                    arrs.add(k * z)
                    if z != 0:
                        arrs.add(k // z)

        if number in arrs:
            answer = i
            return answer

        dp.append(arrs)


    return -1
