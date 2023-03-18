from itertools import accumulate
from bisect import bisect_right

def get_arr(d, p):
    # get_rotated_prefix_sum_with_index
    d = list(accumulate(d[::-1]))[::-1]
    indexed_d = [[a, i]for i, a in enumerate(d)]
    p = list(accumulate(p[::-1]))[::-1]
    indexed_p = [[a, i]for i, a in enumerate(p)]
    return d, indexed_d, p, indexed_p

def solution(cap, n, deliveries, pickups):
    answer = 0
    # final_d: deliveries의 인덱스상, deliver해야하는 집의 위치
    # final_d가 음수이면 deliver할 집이 없는 상태
    final_d, final_p = n - 1, n - 1
    while final_d >= 0 and deliveries[final_d] == 0:
        final_d -= 1
    while final_p >= 0 and pickups[final_p] == 0:
        final_p -= 1
    # final_d와 final_p 모두 음수일 경우, 배달/수거할 집이 없는 상황
    while final_d >= 0 and final_p >= 0:
        answer += max(final_d + 1, final_p + 1) * 2
        deliveries = deliveries[:final_d + 1]
        pickups = pickups[:final_p + 1]
        d, indexed_d, p, indexed_p = get_arr(deliveries, pickups)
        
        # 배달
        if final_d >= 0:
            d_idx = bisect_right(d[::-1], cap)
            procecced_d = indexed_d[::-1][:d_idx]
            procecced_d.sort(key=lambda x:(-x[0], -x[1]))
        
        # 수거
        if final_p >= 0:
            p_idx = bisect_right(p[::-1], cap)
            procecced_p = indexed_p[::-1][:p_idx]
            procecced_p.sort(key=lambda x:(-x[0], -x[1]))
        
        final_d = procecced_d[0][1] - 1 if procecced_d[0][0] > 0 else -1
        final_p = procecced_p[0][1] - 1 if procecced_p[0][0] > 0 else -1
    return answer

# cap = 4
# n = 5
# deliveries = [1, 0, 3, 1, 2]
# pickups = [0, 3, 0, 4, 0]

cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]

print(f'{solution(cap, n, deliveries, pickups)=}')