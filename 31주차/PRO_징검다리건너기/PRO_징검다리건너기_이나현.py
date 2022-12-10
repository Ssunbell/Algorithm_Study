#[프로그래머스_징검다리건너기]
def solution(stones, k):
    s = 0
    e = 199_999
    while s <= e:
        mid = (s + e) // 2
        cnt = 0
        for i in stones:
            if i <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k: #높은 명 수
                e = mid - 1
                break
        else:            #낮은 명 수
            s = mid + 1
    return s

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))