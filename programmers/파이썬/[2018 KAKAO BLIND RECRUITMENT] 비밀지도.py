def solution(n, arr1, arr2):
    leftList = []
    rightList = []
    result = []

    for i in range(n):
        twos = format(arr1[i], 'b')
        twos1 = format(arr2[i], 'b')


        while n > len(twos):
            if n != len(twos):
                twos = '0' + twos

        while n > len(twos1):
            if n != len(twos1):
                twos1 = '0' + twos1

        leftList.append(twos)
        rightList.append(twos1)


    for i in range(n):
        tmp = ''
        for j in range(n):
            if leftList[i][j] == '1' or rightList[i][j] == '1':
                tmp = tmp + '#'
            else:
                tmp = tmp + ' '

        result.append(tmp)

    return result;
