def solution(v):
    frist, last = list(), list()

    for i in range(len(v)):
        frist.append(v[i][0])
        last.append(v[i][1])


    count = len(v)
    frists, lasts = 0, 0
    while count > 0:
        fristText, lastText = frist[0], last[0]
        frist = frist[1:]
        last = last[1:]

        if fristText in frist:
            frist.append(fristText)
            fristText = 0
        else:
            frists = fristText

        if lastText in last:
            last.append(lastText)
            lastText = 0
        else:
            lasts = lastText

        count -= 1

    return [frists, lasts]
