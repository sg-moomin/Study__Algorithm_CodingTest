def solution(phone_book):
# 방법 1 - 틀림
#     checking = True
#     answer = ""

#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] in phone_book[j]:
#                 checking = False
#     return checking

# 방법 2 - 틀림
#     checking = True
#     checktext = ""

#     while len(phone_book) > 0:
#         if checktext == "":
#             i = 0
#             checktext = phone_book[0]
#             phone_book = phone_book[1:]
#         else:
#             if checktext in phone_book[i]:
#                 checking = False
#                 break
#             else:
#                 if len(phone_book) - 1 > i:
#                     i += 1
#                 else:
#                     checktext = ""
#     return checking

# 방법 3 - 틀림
#     checking = True
#     checktext = ""

#     while len(phone_book) > 0:
#         checktext = phone_book[0]
#         phone_book = phone_book[1:]
#         checkstr = (' '.join(phone_book))
#         numbering = checkstr.find(checktext)
#         if numbering == -1:
#             checktext = ""
#         else:
#             checking = False
#             break
#     return checking

    checking = True
    phone_book.sort()

    if phone_book[0] in phone_book[1]:
        checking = False

    return checking
