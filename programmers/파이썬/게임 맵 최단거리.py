# 프로그래머스 > 게임 맵 최단거리
# URL : https://programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    visited = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    x_max, y_max = len(maps), len(maps[0])
    x_dis, y_dis = [1, 0, -1, 0], [0, 1, 0, -1]
    x_frist, y_frist, answer = 0, 0, 1

    startsPoint = deque()
    startsPoint.append((x_frist, y_frist, answer))
    visited[x_frist][y_frist] = True

    while startsPoint:
        x, y, answer = startsPoint.popleft();
        for i in range(len(x_dis)):
            x_now = x + x_dis[i]
            y_now = y + y_dis[i]
            if -1 < x_now < x_max and -1 < y_now < y_max:
                if visited[x_now][y_now] == False and maps[x_now][y_now] == 1:
                    maps[x_now][y_now] = answer + 1
                    visited[x_now][y_now] = True
                    startsPoint.append((x_now, y_now, answer + 1))

    if not visited[x_max-1][y_max-1]:
        return -1
    else:
        return maps[x_max-1][y_max-1]
