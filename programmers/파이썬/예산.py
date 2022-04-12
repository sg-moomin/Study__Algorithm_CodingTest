# 프로그래머스 > 예산
# url : https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(arr, bug):
    arr = sorted(arr)
    answer = 0
    budgets = 0

    for i in arr:
        if (budgets + i) <= bug:
            budgets = budgets + i
            answer += 1

    return answer
