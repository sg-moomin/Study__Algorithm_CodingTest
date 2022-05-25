# 백준 2583_영역구하기
from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for i in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []
area = 0

for i in range(k):
    sx, sy, ex, ey= map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            graph[i][j] = 1

def bfs(i, j):
    queue = deque([[i, j]])
    graph[i][j] = 1
    count = 1

    while queue:
        x, y = queue.popleft()
        for z in range(4):
            nowx = x + dx[z]
            nowy = y + dy[z]
            if nowx < 0 or nowx > m-1 or nowy < 0 or nowy > n-1 :
                continue
            if graph[nowx][nowy] == 0:
                queue.append([nowx, nowy])
                graph[nowx][nowy] = 1
                count += 1

    return count


for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))
            area += 1

print(area)
result.sort()
answer = ""
for i in result:
    answer += str(i) + " "

print(answer)          
