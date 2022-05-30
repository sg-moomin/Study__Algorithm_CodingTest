# 백준 > 7568_덩치 
# url : https://www.acmicpc.net/problem/7568

N = int(input())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))


for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end = ' ')
