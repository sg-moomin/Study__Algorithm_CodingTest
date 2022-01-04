def solution(n):
    result = []
    count = n
    while count > 0:
        tmp = count % 3
        result.append(tmp)
        count = int(count / 3)

    print(result)

    i, check = -1, 0
    answer = 0
    while check < len(result):
            answer += (result[i] * (3 ** check))
            i -= 1
            check += 1

    return answer
