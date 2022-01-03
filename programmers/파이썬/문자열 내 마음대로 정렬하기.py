def solution(s, n):
    # strings.sort()
    # strings.sort(key=lambda x : (x[n]))
    # return strings
    result = []
    s.sort()

    for i in range(len(s)):
        result.append([s[i], s[i][n]])

    result.sort(key=lambda x : (x[1]))

    answer = []
    for i in range(len(result)):
        answer.append(result[i][0])

    return answer
