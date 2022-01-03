# for문과 while문의 차이
def solution(arr):
    answer = []
    count = 0
#     while len(arr) > 0:
#         temp = arr[0]
#         if len(answer) == 0:
#             answer.append(temp)
#         elif answer[count] == temp:
#             arr = arr[1:]
#             continue
#         else:
#             answer.append(temp)
#             count += 1

#         arr = arr[1:]

    for i in range(len(arr)):
        if len(answer) != 0:
            temp = arr[i]
            if answer[count] != temp:
                answer.append(temp)
                count += 1
        else:
            answer.append(arr[i])


    return answer
