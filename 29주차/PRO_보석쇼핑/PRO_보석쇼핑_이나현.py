#[프로그래머스_보석쇼핑]
from collections import defaultdict
def solution(gems):
    L = len(gems)
    L_unique = len(set(gems))
    start = 0
    gem_count = defaultdict(lambda : 0)
    answer = [1, L]
    #["AA", "AB", "AC", "AA", "AC"]
    for end in range(L):
        gem_count[gems[end]] += 1
        if len(gem_count.keys()) < L_unique:
            continue
        while gem_count[gems[start]] - 1 > 0:
            gem_count[gems[start]] -= 1
            start += 1
        if end - start < answer[1] - answer[0]:
            answer[0], answer[1] = start+1, end+1
    return answer

print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution([1,2,3,4,1,2,3,4]))