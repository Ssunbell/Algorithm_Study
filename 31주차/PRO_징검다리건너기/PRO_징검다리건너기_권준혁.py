def solution(stones, k):
    def check(threshold: int):
        cnt = 0
        for num in stones:
            if num <= threshold:
                cnt += 1
                if cnt >= k:
                    return False
            else:
                cnt = 0
        else:
            return True
    s, e = 1, 200_000_000
    while(s <= e):
        mid = (s + e) // 2
        if check(mid):
            s = mid + 1
        else:
            e = mid - 1
    return s