def solution(n):
    answer = 0
    s = str(n)
    for i in range(len(s)):
        answer += int(s[i])

    return answer
