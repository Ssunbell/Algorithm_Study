from collections import deque

n, k = map(int, input().split())

# 탐색할 큐
q = deque()
q.append(n)

# 몇번만에 갔는지 확인
# 100000은 안되고 100001은 통과. 이유는 모르겠다.
# depth_chart = [0] * 100000
depth_chart = [0] * 100001

while q:
    curr = q.popleft()

    # 종료지점에 오면 종료
    if curr == k:
        break

    # 다음 지점 큐에 저장
    next_list= [curr-1, curr+1, curr*2]
    for next in next_list:
        if 0 <= next <= 100000 and depth_chart[next] == 0:
            q.append(next)
            depth_chart[next] = depth_chart[curr] + 1

print(depth_chart[k])

# 딕셔너리로 구현, 시간초과. 딕셔너리의 시간복잡도가 높아서 그런듯.
# from collections import deque

# n, k = map(int, input().split())

# # 탐색할 큐
# q = deque()
# q.append(n)

# # 몇번만에 갔는지 확인
# depth_chart = {n:0}

# while q:
#     curr = q.popleft()

#     # 종료지점에 오면 종료
#     if curr == k:
#         break

#     # 다음 지점 큐에 저장
#     next_list= [curr-1, curr+1, curr*2]
#     for next in next_list:
#         try :
#             depth_chart[next]
#         except:
#             q.append(next)
#             depth_chart[next] = depth_chart[curr] + 1

# print(depth_chart[k])