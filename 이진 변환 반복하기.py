def solution(s):
    answer = ""
    count, zeroCount = 0, 0
    tmp = 0

    while s != "1":
        print(count, zeroCount, s)
        tmp = 0
        for i in range(len(s)):
            if s[i] == "1":
                tmp += 1

        zeroCount += len(s) - tmp
        temps = []
        for i in range(tmp):
            if tmp == 0:
                break

            nums = tmp % 2 
            temps.append(str(nums))
            tmp = tmp // 2

        s = "".join(temps)
        count += 1

    return [count, zeroCount]
