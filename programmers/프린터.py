# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
def solution(pro, location):
    result = deque()
    stack = deque()
    count = 0
    maxSize = 0

    for i in range(len(pro)):
        stack.append(pro[i])
        result.append(i)

    checkPoint = result[location]

    while True:
        print(stack, result, location, count, maxSize)
        maxSize = max(list(stack))
        tmp = stack.popleft()
        if tmp != maxSize:
            stack.append(tmp)
            result.rotate(-1)
        else:
            count += 1
            if tmp == pro[location] and result[0] == checkPoint:
                break

            result.popleft()

    return count

pro = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(pro, location))
