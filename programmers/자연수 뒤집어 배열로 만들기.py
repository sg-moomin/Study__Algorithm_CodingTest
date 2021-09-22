def solution(n):
    answer = []
    s = str(n)

    for i in range(len(s)):
        answer.append(int(s[i]))

    answer.reverse()
    return answer
