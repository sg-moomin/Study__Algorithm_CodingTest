import math
def solution(W,H):
#  1번째 접근 방법
#     answer = 0
#     count = 0
#     checkList = [False] * (H + 1)

#     if W == H:
#         return W*H - W
#     elif W == 1 or H == 1:
#         return 0


#     for i in range(1, W + 1):
#         n = int((H / W)* i)
#         checkList[n] = True

#     checkOne = checkList.count(True)
#     checkTwo = checkList.count(False) - 1

#     answer = (W * H) - (checkOne + (checkTwo * 2))

#     return answer

    answer = 0


    answer = (W * H) - (W + H - math.gcd(W, H))
    return answer
