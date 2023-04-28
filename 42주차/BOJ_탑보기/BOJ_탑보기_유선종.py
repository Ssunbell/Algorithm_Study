from collections import deque

n = int(input())
building = list(map(int, input().split()))

cnt = [0] * (n + 1)
near = [[float('inf'), float('inf')] for _ in range(n + 1)] # [건물번호, 건물거리]

def count_building(building, mode):
    stack = [] # [건물번호, 건물 높이]
    for idx, b in enumerate(building, 1) if mode=='left' else reversed(list(enumerate(building, 1))):
        while stack and stack[-1][1] <= b:
            stack.pop()
        cnt[idx] += len(stack)

        if len(stack) > 0:
            dist = abs(stack[-1][0] - idx) # 가장 가까운 빌딩과의 거리
            if dist < near[idx][1]:
                near[idx][0] = stack[-1][0]
                near[idx][1] = dist
            elif dist == near[idx][1] and stack[-1][0] < near[idx][0]: # 거리가 같고 건물 번호가 더 작은 경우
                near[idx][0] = stack[-1][0]

        stack.append([idx, b])

count_building(building, 'left')
count_building(building, 'right')

for i in range(1, n + 1):
    if cnt[i] > 0:
        print(cnt[i], near[i][0])
    else:
        print(0)