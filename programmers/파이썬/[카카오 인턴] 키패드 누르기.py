def solution(numbers, hand):
    leftHand = 10   # i = *
    rightHand = 12  # i = #
    lx, rx = 0, 0, 0
    ly, ry = 0, 0, 0
    leftDis = 0
    rightDis = 0

    result = ""

    for i in numbers:
        if i == 0:
            i = 11
        if i == "#":
            i = 12
        if i == "*":
            i = 10

        if i % 3 == 1:
            result += "L"
            leftHand = i

        elif i % 3 == 0:
            result += "R"
            rightHand = i
        else:
            lx = (abs(i - leftHand)) // 3
            ly = (abs(i - leftHand)) % 3
            rx = (abs(i - rightHand)) // 3
            ry = (abs(i - rightHand)) % 3
            leftDis = (lx + ly)
            rightDis = (rx + ry)

            if leftDis > rightDis:
                print("leftDis > rightDis")
                result += "R"
                rightHand = i
            elif rightDis > leftDis:
                print("leftDis < rightDis")
                result += "L"
                leftHand = i
            elif rightDis == leftDis:
                if hand == "right":
                    result += "R"
                    rightHand = i
                else:
                    result += "L"
                    leftHand = i

    return result
