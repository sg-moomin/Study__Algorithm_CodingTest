# 적록색약
# url : https://www.acmicpc.net/problem/10026

n = int(input())
sys.setrecursionlimit(10**7)
arr = []
red_arr = [['0'] * n for i in range(n)]
visitedG = [[False for i in range(n)] for j in range(n)]
visitedN = [[False for i in range(n)] for j in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count_N = 0
count_G = 0

for i in range(n):
    arr.append(list(input()))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            red_arr[i][j] = 'R'
        else:
            red_arr[i][j] = arr[i][j]


def noDfs(strs, x, y):
    visitedN[x][y] = True
    for i in range(4):
        nowX = x + dx[i]
        nowY = y + dy[i]
        if nowX >= 0 and nowX < n and nowY >= 0 and nowY < n:
            if not visitedN[nowX][nowY] and arr[nowX][nowY] == strs:
                noDfs(strs, nowX, nowY)


def dfs(strs, x, y):
    visitedG[x][y] = True
    for i in range(4):
        nowX = x + dx[i]
        nowY = y + dy[i]
        if nowX >= 0 and nowX < n and nowY >= 0 and nowY < n:
            if visitedG[nowX][nowY] == False:
                if strs == 'R' or strs == 'G':
                    if arr[nowX][nowY] == 'G'or arr[nowX][nowY] == 'R':
                        dfs(strs, nowX, nowY)
                else:
                    if arr[nowX][nowY] == strs:
                        dfs(strs, nowX, nowY)



for i in range(n):
    for j in range(n):
        if not visitedN[i][j]:
            count_N += 1
            noDfs(arr[i][j], i, j)
        if not visitedG[i][j]:
            count_G += 1
            dfs(arr[i][j], i, j)

print(count_N, count_G)
