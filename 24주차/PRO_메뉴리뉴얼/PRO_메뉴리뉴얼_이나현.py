#[메뉴 리뉴얼]
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    table = defaultdict(lambda:defaultdict(lambda:0))
    for o in orders:
        o = sorted(o)
        for l in range(1, len(o)+1):
            for c in combinations(o, l):
                table[l][c] += 1
    answer = []
    for c in course:
        values = table[c].values()
        if len(values) == 0:
            continue
        max_value = max(values)
        if max_value < 2:
            continue
        for comb in table[c]:
            if table[c][comb] == max_value:
                answer.append("".join(comb))
    answer.sort()
    return answer

test = [[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]],  #["AC", "ACDE", "BCFG", "CDE"]
        [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]], #["ACD", "AD", "ADE", "CD", "XYZ"]
        [["XYZ", "XWY", "WXA"], [2,3,4]]] #["WX", "XY"]
for o, c in test:
    print(solution(o,c))