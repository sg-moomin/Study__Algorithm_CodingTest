def solution(phone_number):
    star = "*"
    result = []

    for i in range(len(phone_number)):
        if i == len(phone_number) - 4:
            result += phone_number[i:]
            break
        else:
            result += star

    answer = "".join(result)
    return answer
