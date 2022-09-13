import sys
input = sys.stdin.readline
N = int(input())
# 크레인 최대하중 내림차순 정렬
limits = sorted(map(int, input().split()), reverse=True)
M = int(input())
# 운반해야 할 박스 무게별로 내림차순 정렬
box_weight = sorted(map(int, input().split()), reverse=True)

time = 0
# 가장 무거운 박스를 옮길 수 있는 방법이 없는 경우
if limits[0] < box_weight[0]:
    time = -1
else:
    # 운반해야 할 박스가 존재할 동안 반복
    while box_weight:
        # 옮길 수 있는 무게가 높은 크레인부터 반복
        for i in limits:
            if not box_weight or i < box_weight[-1]:
                break
            else:
                # 박스를 옮길 수 있을 경우
                for j in range(M):
                    if i >= box_weight[j]:
                        box_weight.pop(j)
                        break
        time += 1
print(time)

'''
크레인 정보와 박스 무게 정보를 미리 내림차순으로 정렬하면 옮길 수 없는 경우가 나왔을 때 break하여 나머지 연산을 skip할 수 있다.
예를들어 [5, 4, 3, 2, 1]인 크레인으로 [4, 4]를 옮기는 과정은 다음과 같다.
1. 첫번째 박스를 옮길 수 있는 크레인을 찾는다 => 두번째 크레인에 적재
2. 두번째 박스를 옮길 수 있는 크레인을 연속해서 찾는다. 5, 4는 첫번째 박스 옮길 때 이미 고려했으므로 3부터 시작한다.
3. 최대 하중 3인 크레인으로 4를 옮길 수 없으므로 break하고 5부터 다시 시작한다.
'''
