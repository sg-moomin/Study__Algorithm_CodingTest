def solution(s):

    if len(s) % 2 == 0:
        num1 = int(len(s) / 2)
        num2 = num1 - 1
        return s[num2] + s[num1]
    else:
        num1 = int(len(s) / 2)
        return s[num1]
