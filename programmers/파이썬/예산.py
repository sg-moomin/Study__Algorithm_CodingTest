import itertools

pool = ['1','3','2','5','4']
lists = list(map(''.join, itertools.permutations(pool)))
print(lists)
# print(int(lists[1][1]) + int(lists[1][2]))
