def solution(stones, k):
    s, e = 1, 200000000
    while s <= e:
        m, cnt = (s + e) // 2, 0
        for stone in stones:
            if stone - m <= 0:
                cnt += 1
                if cnt >= k:
                    e = m - 1
                    break
            else:
                cnt = 0
        else:
            s = m + 1
    return s