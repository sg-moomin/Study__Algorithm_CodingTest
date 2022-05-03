from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        result_tmp = []
        for j in orders:
            j = sorted(j)
            result_tmp.extend(list(combinations(j, i)))

        count = Counter(result_tmp)

        if len(count) > 0:
            max_menu = max(list(count.values()))
            if max_menu >= 2:
                for value, key in count.items():
                    if key == max_menu:
                        answer.append(''.join(value))

    return sorted(answer)
