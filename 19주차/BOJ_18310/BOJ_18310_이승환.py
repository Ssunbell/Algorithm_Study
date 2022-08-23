from collections import deque

n = int(input())
houses = deque(map(int,input().split()))
houses = sorted(houses)


# left_num은 현재 위치에서 왼쪽에 있는 집의 개수
# right_num은 현재 위치에서 오른쪽에 있는 집의 개수 + 1
# 이전 장소와 지금 장소의 차이를 diff라하면
# curr_distance += left_num * diff
# curr_distance -= right_num * diff
# curr_disctance가 작아지면 계속, 같거나 크면 멈춤
curr = 0
curr_distance = sum(houses)
left_num = 0
right_num = len(houses)
for place in houses:
    diff = place - curr
    next_distance = curr_distance + (left_num * diff) - (right_num * diff)
    if next_distance < curr_distance:
        curr_distance = next_distance
        left_num += 1
        right_num -= 1
        curr = place
    else:
        break

print(curr)

#________________________________________________________#

# from collections import deque

# n = int(input())
# houses = deque(map(int,input().split()))
# houses = sorted(houses)
# answer = houses[int(len(houses)/2)-1]

# print(answer)

#________________________________________________________#

# from collections import deque

# n = int(input())
# houses = deque(map(int,input().split()))

# result = deque()
# for place in houses:
#     output = deque(map(lambda x:abs(x - place), houses))
#     result.append(sum(output))

# print(houses[result.index(min(result))])

#________________________________________________________#

# n = int(input())
# houses = list(map(int,input().split()))

# avg_place = sum(houses)/len(houses)

# min_distance = 9999999

# for place in houses:
#     if abs(avg_place - place) < min_distance:
#         min_distance = abs(avg_place - place)
#         answer = place

# print(answer)