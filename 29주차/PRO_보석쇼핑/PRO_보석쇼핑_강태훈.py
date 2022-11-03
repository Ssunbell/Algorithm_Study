def solution(gems):
    gemset = set(gems)
    gemlen, gemsetlen = len(gems), len(gemset)
    s, e, pocket_size = 0, 0, 1
    pocket = {i: 0 for i in gemset}
    pocket[gems[0]] += 1
    answer = [1, gemlen]
    while s <= e and e < gemlen:
        if pocket_size == gemsetlen:
            if answer[1]-answer[0] > e-s:
                answer = [s+1, e+1]
            pocket[gems[s]] -= 1
            if pocket[gems[s]] == 0:
                pocket_size -= 1
            s += 1
        else:
            e += 1
            if e >= gemlen:
                break
            pocket[gems[e]] += 1
            if pocket[gems[e]] == 1:
                pocket_size += 1
    return answer


tc = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
]
for c in tc:
    print(solution(c))
