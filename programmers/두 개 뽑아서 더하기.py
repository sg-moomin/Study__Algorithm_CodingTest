#https://programmers.co.kr/learn/courses/30/lessons/68644
#  첫번째 시도 - 4번 5번 케이스 불 일치
# def solution(numbers):
#     answer = []
#     result = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             result.append(numbers[i] + numbers[j])
#     answer = list(set(result))
#     return answer

def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            tmp = numbers[i] + numbers[j]
            if not tmp in result:
                result.append(tmp)
    result.sort()
    return result
