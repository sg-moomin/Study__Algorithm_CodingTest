def solution(s):
    result = ""
    count = 0
    for i in s:
        if i != " ":
            if count % 2 == 0:
                tmp = str(i)
                result += tmp.upper()
            else:
                tmp2 = str(i)
                result += tmp2.lower()
            count += 1

        else:
            result += " "
            count = 0

    return result



# s = "try hello world"
# num = s.split()
# print(num)
# result = ""
# count = len(num)
# for i in num:
#     for j in range(len(i)):
#         if j % 2 == 0:
#             tmp = str(i[j])
#             result += tmp.upper()
#         else:
#             tmp2 = str(i[j])
#             result += tmp2.lower()
#     count -= 1
# 
#     if count != 0:
#         result += " "
#
# result.rstrip()
