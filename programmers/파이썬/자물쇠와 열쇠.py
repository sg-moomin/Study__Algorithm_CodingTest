# URL : https://programmers.co.kr/learn/courses/30/lessons/60059
# 프로그래머스 > 2020 KAKAO BLIND RECRUITMENT > 자물쇠와 열쇠


import numpy as np

def rotate_key(keys):
    rotated = np.array(list(zip(*keys[::-1])))
    return rotated

def solution(key, lock):
    key_num = len(key)
    lock_num = len(lock)

    arrays = [[0] * (key_num * lock_num) for i in range(key_num * lock_num)]
    for i in range(lock_num):
        for j in range(lock_num):
            arrays[key_num+i][key_num+j] = lock[i][j]

    key_rotate = key
    for i in range(4):
        key_rotate = rotate_key(key_rotate)
        for j in range(key_num + lock_num):
            for z in range(key_num + lock_num):
                key_chk = 0
                for a in range(key_num):
                    for b in range(key_num):
                        arrays[j+a][z+b] += key_rotate[a][b]

                for a in range(lock_num):
                    for b in range(lock_num):
                        if arrays[key_num+a][key_num+b] == 1:
                            key_chk += 1

                if key_chk == key_num ^ 2:
                    return True

                for a in range(key_num):
                    for b in range(key_num):
                        arrays[j+a][z+b] -= key_rotate[a][b]


    return False
