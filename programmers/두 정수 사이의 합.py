def solution(a, b):
    result = 0
    if a > b:
        a, b = b, a

    for i in range(a, b+1):
        result += i

    return result
