def solution(board, moves):
    lists = []
    countNumber = 0
    answer = 0


    for i in range(len(moves)):
        temp = int(moves[i])
        for j in range(len(board[temp - 1])):
            if board[j][temp - 1] != 0:
                countNumber += 1
                checknum = board[j][temp - 1]
                lists.append(checknum)
                board[j][temp - 1] = 0
                break;



        if len(lists) > 1 and lists[countNumber - 1] == lists[countNumber - 2]:
            lists.pop(-1)
            lists.pop(-1)
            answer += 2
            countNumber -= 2


    
    return answer
