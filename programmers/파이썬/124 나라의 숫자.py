# 틀렸다고 뜨는 코드 - 아마 answers++을 하면 순서가 달라져서 그런듯..ㄷㄷ
# def solution(n):

#     answers = ""
#
#     while n:
#         if n % 3 == 0:
#             answers += str(4)
#             n = (n // 3) - 1
#         else:
#             answers += str(n % 3)
#             n = n // 3
#
#     return answers


def solution(n):
    answers = ""

    while n:
        if n % 3 == 0:
            answers = str(4) + answers
            n = (n // 3) - 1
        else:
            answers = str(n % 3) + answers
            n = n // 3

    return answers


n = 13
print(solution(13))
