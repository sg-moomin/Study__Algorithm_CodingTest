# 프로그래머스 > 오픈채팅방
# URL : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):

    resultList = []
    resultUsrId = {}

    for i in record:
        temp = i.split()
        check = temp[0]
        usrId = temp[1]

        if check == "Enter":
            resultUsrId[usrId] = temp[2]
            resultList.append((check, usrId))
        if check == "Change":
            resultUsrId[usrId] = temp[2]
        if check == "Leave":
            resultList.append((check, usrId))



    usrCount = ""
    checkCount = ""

    answer = list()
    for i in range(len(resultList)):
        checkCount = resultList[i][0]
        usrCount = resultList[i][1]
        resultCheck = ""

        if(checkCount == "Enter"):
            resultCheck = resultUsrId[usrCount] + "님이 들어왔습니다."
        else:
            resultCheck = resultUsrId[usrCount] + "님이 나갔습니다."

        answer.append(resultCheck)




    return answer
