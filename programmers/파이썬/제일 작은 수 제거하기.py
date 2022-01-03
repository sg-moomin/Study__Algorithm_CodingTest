def solution(arr):

    result = 0
    tempArr = []
    for i in arr:
        tempArr.append(i)

    tempArr.sort()
    checkNumber = tempArr[0]

    if len(tempArr) == 1:
        return [-1]
    else:
        arr.remove(checkNumber)

    return arr
