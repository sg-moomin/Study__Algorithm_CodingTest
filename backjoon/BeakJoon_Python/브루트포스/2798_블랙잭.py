# 백준 > 2798_블랙잭
# url : https://www.acmicpc.net/problem/2798
from itertools import combinations

x, y = input().split()
arr = list(map(int, input().split()))
maxs = 0

for i in combinations(arr, 3):
    tmp = sum(i)
    if tmp <= int(y):
        if maxs < tmp:
            maxs = tmp

print(maxs)
