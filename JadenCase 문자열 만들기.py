def solution(s):
    lists = list(s.split())
    tmp = ""
    fristName, lastName = "", ""
    answer_list = [""] * len(lists)
    answer = ""
    for i in range(len(lists)):
        tmp = lists[i]
        fristName = str(lists[i][0])
        lastName = str(lists[i][1:])
        fristName = fristName.upper()
        lastName = lastName.lower()
        answer_list[i] = fristName + lastName

    answer = ' '.join(answer_list)
    return answer
