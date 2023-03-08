#프로그래머스_외벽점검
#완전탐색(조합), 안갈 수 있는 외벽사이거리에 집중
#친구가 1명일 때 외벽 사이 거리들 중 하나는 안갈 수 있다.
#step1 외벽 위치 -> 외벽 사이 거리 구한다.
#step2 친구 수만큼 for문을 돈 후 해당 친구수일 때 가야하는 외벽사이구간의 조합을 구할 수 있다.
#step3 만약 해당 친구수일 때 모두 갈 수 있는 case가 있다면 해당 친구수 바로 리턴

from itertools import combinations

#제외된 외벽사이 거리를 제외한 구간의 길이들을 리스트로 반환하는 함수
#즉, 친구들이 가야하는 구간의 길이들을 리스트로 반환하는 함수 (리스트는 내림차 정렬됨)
def get_section_sum(arr, start) -> list:
    section_sum = []
    idx = start
    tmp_sum = 0
    for _ in range(len(arr)+1):
        tmp_sum += arr[idx]
        if arr[idx] == 0:
            section_sum.append(tmp_sum)
            tmp_sum = 0
        idx = (idx + 1) % len(arr)
    return sorted(section_sum, reverse=True)

def solution(n, weak, friend):
    len_weak = len(weak)
    between = [weak[i+1] - weak[i] for i in range(len_weak-1)] + [n+weak[0]-weak[-1]]
    friend.sort(reverse=True)
    for i in range(1,len(friend)+1):                      #i는 친구 수를 나타냄
        for comb in combinations(range(len(between)), i): #해당 친구수일 때 안갈 수 있는 외벽사이거리 조합
            tmp_between = between[:]
            for j in comb:
                tmp_between[j] = 0
            section_sum = get_section_sum(tmp_between, comb[0])
            for j in range(i):
                if friend[j] < section_sum[j]:
                    break
            else:
                return i
    return -1


print(solution(16, [1,2,3,4,5,7,8,10,11,12,14,15], [4,2,1,1]))
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
print(solution(500, [100,200,300,400,500], [1,1,1,1,1]))