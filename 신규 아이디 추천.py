import re
def solution(new_id):
    # 1단계
    # for i in range(len(new_id)):
    #     if ord(new_id[i]) >= ord('A') and ord(new_id[i]) <= ord('Z'):
    #         new_id = new_id.replace(new_id[i], chr(ord(new_id[i]) + 32))
    new_id = new_id.lower()


    # 2단계
    # temp = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
    temp2 = ""
    for i in range(len(new_id)):
        if ord('a') <= ord(new_id[i]) and ord('z') >= ord(new_id[i]):
            temp2 += new_id[i]
        elif ord('0') <= ord(new_id[i]) and ord('9') >= ord(new_id[i]):
            temp2 += new_id[i]
        elif ord('-') <= ord(new_id[i]) and ord('.') >= ord(new_id[i]):
            temp2 += new_id[i]
        elif ord('_') == ord(new_id[i]):
            temp2 += new_id[i]

    temp = temp2

    # 3단계
    while ".." in temp:
        temp = temp.replace("..", ".")

    # 4단계 - 문자열은 replace로 제거하는건 힘듬

    FristCheck, LastCheck = False, False

    if ord(temp[0]) == ord('.'):
        FristCheck = True
        # temp = temp[1:]
    if ord(temp[-1]) == ord('.'):
        LastCheck = True
        # temp = temp[:-1]

    if FristCheck == True:
        temp = temp[1:]
    if LastCheck == True:
        temp = temp[:-1]

    # 5단계
    if temp == "":
        temp = "a"

    # 6단계
    if len(temp) >= 16:
        temp = temp[:15]
        if ord(temp[-1]) == ord('.'):
            temp = temp[:-1]

    #7단계
    if len(temp) <= 2:
        while len(temp) < 3:
            temp = temp + temp[-1]


    return temp





# # 초기 버전 -> 문제 틀림
# import re
# new_id = "abcdefghijklmn.p"
# # 1단계
# for i in range(len(new_id)):
#     if ord(new_id[i]) >= 65 and ord(new_id[i]) < 91:
#         new_id = new_id.replace(new_id[i], chr(ord(new_id[i]) + 32))
#
# # 2단계
# temp = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
#
# # 3단계
# while ".." in temp:
#     temp = temp.replace("..", ".")
#
# # 4단계 - 문자열은 replace로 제거하는건 힘듬
# print(temp[0], temp[-1])
# if ord(temp[0]) == 46:
#     temp = temp[1:]
# elif ord(temp[-1]) == 46:
#     print(temp)
#     temp = temp[:-1]
#
# # 5단계
# if temp == "":
#     temp = a
#
# # 6단계
# if len(temp) >= 16:
#     print("6", temp)
#     temp = temp[:15]
#     print(temp[-1])
#     if ord(temp[-1]) == 64:
#         print(temp)
#         temp = temp[:-1]
#
# #7단계
# if len(temp) <= 2:
#     while len(temp) < 3:
#         temp = temp + temp[-1]
#
# print(temp)
