# 데모 테스트
v = [[1, 1], [2, 2], [1, 2]]

FristCheck, LastCheck = [], []
result = [0] * 2

for i in range(len(v)):
    result[0] ^= v[i][0]
    result[1] ^= v[i][1]

print(result)
