# 프로그래머스 > 행렬 테두리 회전하기
# URL : https://programmers.co.kr/learn/courses/30/lessons/77485


def solution(rows, columns, queries):
    answer = []
    visited = []
    for i in range(rows):
        visited_tmp = []
        for j in range(i*columns+1, (i+1)*columns+1):
            visited_tmp.append(j)

        visited.append(visited_tmp)


    for up_que, left_que, down_que, right_que in queries:
        up, left, down, right = up_que-1, left_que-1, down_que-1, right_que-1
        starts = visited[up][left]
        result = starts

        for i in range(up, down):    # 상
            visited [i][left] = visited[i+1][left]
            result = min(result, visited[i+1][left])

        for j in range(left, right): # 좌
            visited[down][j] = visited[down][j+1]
            result = min(result, visited[down][j+1])

        for k in range(down, up, - 1):  # 하
            visited[k][right] = visited[k-1][right]
            result = min(result, visited[k-1][right])

        for l in range(right, left, - 1):  # 우
            visited[up][l] = visited[up][l-1]
            result = min(result, visited[up][l-1])

        visited[up][left+1] = starts
        answer.append(result)

    return answer
