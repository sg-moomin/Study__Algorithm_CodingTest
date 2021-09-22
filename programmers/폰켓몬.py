def solution(nums):
    result = len(nums) // 2
    nums = list(set(nums))
    answer = 0

    if result >= len(nums):
        answer = len(nums)
    else:
        answer = result

    return answer
