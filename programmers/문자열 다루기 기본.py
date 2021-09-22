def solution(s):

    if len(s) != 4 and len(s) != 6:
        return False

    check = True
    for i in s:
        if ord(i)>= 48 and 57 >= ord(i):
            continue
        else:
            check = False
            break

    return check
