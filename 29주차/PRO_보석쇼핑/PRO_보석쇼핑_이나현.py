#[프로그래머스_보석쇼핑]
from collections import defaultdict
def solution(gems):
    L = len(gems)
    L_unique = len(set(gems))
    start = 0
    count = defaultdict(lambda : 0)
    answer = [1, L]
    for end in range(L):
        count[gems[end]] += 1
        if len(count.keys()) < L_unique:
            continue
        while count[gems[start]] - 1 > 0:
            count[gems[start]] -= 1
            start += 1
        if end - start < answer[1] - answer[0]:
            answer[0], answer[1] = start+1, end+1
    return answer

print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution([1,2,3,4,1,2,3,4]))