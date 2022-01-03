def solution(skil, skill_trees):
    skilCount = [0] * 26

    count = 0
    for i in range(len(skil)):
        tmp = ord(skil[i]) - ord("A")
        skilCount[tmp] = i + 1


    for i in skill_trees:
        result = ""
        for j in range(len(i)):
            tmp2 = ord(i[j]) - ord("A")
            if skilCount[tmp2] != 0:
                result += i[j]


        if result in skil[:len(result)]:
            count += 1

    return count

skil = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skil, skill_trees))
