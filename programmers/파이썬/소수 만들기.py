def solution(num):
    import itertools
    from itertools import permutations

    numbers = []
    answer = 0
    nums = list(itertools.combinations(num, 3))
    for i in range(len(nums)):
        numbers.append(sum(nums[i]))

    for i in numbers:
        count = 2
        for j in range(2, i):
            if i % j == 0:
                continue
            else:
                count+=1

        if count == i:
            answer += 1

    return answer
