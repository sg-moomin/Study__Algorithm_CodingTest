def solution(s):
    defaultCheck = False

    if s.find('p') == -1 and s.find('y') == -1:
        defaultCheck = True
        return defaultCheck

    pCheck, yCheck = 0, 0
    PCheck, YCheck = 0, 0

    for i in range(len(s)):
        if s[i] == "p":
            pCheck += 1
        elif s[i] == "y":
            yCheck += 1
        elif s[i] == "P":
            PCheck += 1
        elif s[i] == "Y":
            YCheck += 1
        else:
            continue

    if (pCheck + PCheck) == (yCheck + YCheck):
        return True
    else:
        return False
