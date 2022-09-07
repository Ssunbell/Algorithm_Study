import sys

input_s = lambda : sys.stdin.readline().strip()

n, k = map(int,input_s().split())
team = list(int(input_s()) for _ in range(n))

start = min(team)
end = max(team) + k

while start <= end:
    mid = int((start + end) / 2)

    need_level = 0

    for level in team:
        need_level += max(0, mid-level)

    # mid-1, mid+1을 해야 하는 이유를 모르겠음.
    if need_level > k:
        end = mid -1
    else:
        start = mid +1
        answer = mid

    # mid-1, mid+1을 하지 않았을 경우 무한루프에서 탈출하는 조건.
    # if start + 1 == end:
    #     break

print(answer)

# 시간초과, 너무 많은 조건문을 사용해 시간초과나는듯
# while True:
#     mid = int((start + end) / 2)

#     need_level = 0
#     num_min_level = 0

#     for level in team:
#         if mid-level > 0:
#             need_level += (mid-level)
#             num_min_level += 1

#     left_level = k-need_level

#     if need_level > k:
#         end = mid
#     elif need_level <= k and left_level >= num_min_level:
#         start = mid
#     elif need_level <= k and left_level < num_min_level:
#         answer = mid
#         break

# print(answer)