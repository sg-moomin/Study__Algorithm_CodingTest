

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
participant.sort()
completion.sort()

def solution(participant, completion):
    answer = ""
    # 시간초과 문제
    # i = 0
    # while len(participant) > 1:
    #     count = i
    #     if completion[0] == participant[i]:
    #         participant.pop(i)
    #         i = 0
    #     elif count == len(participant) - 1:
    #         tmp = completion[0]
    #         completion.pop(0)
    #         completion.append(tmp)
    #         i = 0
    #     else:
    #         i += 1

    # 시간초과 문제
    #     participant.sort()
    #     completion.sort()


    #         for i in completion:
    #             participant.remove(i)

    #         answer = (''.join(participant))
    #         return answer

    #  시간초과
    #     participant.sort()
    #     completion.sort()

    #     checkC = {}
    #     checkP = {}


    #     for i, v in enumerate(participant):
    #         checkP.update({v:participant.count(v)})

    #     for i, v in enumerate(completion):
    #         checkC.update({v:completion.count(v)})


    #     answer = ""
    #     result = list(checkC.items())
    #     for i in checkP.items():
    #         if i not in result:
    #             answer = i[0]

    #     return answer

    # 성공
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]

print(solution(participant, completion))
