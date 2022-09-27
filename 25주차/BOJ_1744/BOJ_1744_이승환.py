n = int(input())
nums = [int(input()) for _ in range(n)]

def solution(n,nums):
    nums = sorted(nums, key=abs, reverse= True)
    answer = 0
    neg = []
    pos = []
    for num in nums:
        if num < 1:
            neg.append(num)
            if len(neg) == 2:
                answer += (neg[0] * neg[1])
                neg = []
        elif num > 1:
            pos.append(num)
            if len(pos) == 2:
                answer += (pos[0] * pos[1])
                pos = []
        elif num == 1:
            answer += num
    answer += (sum(pos) + sum(neg))
    return answer

print(solution(n,nums))

# 수를 전부 절대값 기준으로 정렬한다
# 절대값이 큰 수 순서대로 각각 양수, 음수 리스트에 저장하고
# 리스트의 길이가 2가되면 두 수를 곱하고 더한 다음 리스트 초기화
# 만약 1일경우에는 더하는 것이 더 크기 때문에 리스트에 추가하지 않고 더함
# 양수,음수 리스트에 남은걸 다 더해주면 정답.


# case = [[5,[3,9,4,3,3],48],
#         [2,[2,1],3],
#         [5,[-3,-2,-1,1,2],8],
#         [3,[-6,-5,-1],29],
#         [5,[1,1,1,1,1],5],
#         [13,[-10,-9,-8,-7,-6,-5,1,2,3,4,5,6,7],245],
#         [10,[-5,-4,-3,0,1,2,3,4,5,6],65],
#         [10,[-10,-9,-8,-7,-6,0,1,2,3,4],161],
#         [5,[-1,-2,0,0,0],2],
#         [5,[-5,-4,-3,-2,-1],25]]

# i = 0
# for c in case:
#     i += 1
#     n,nums,result = c
#     answer = solution(n,nums)
#     print(f"정답 : {result}, 나의 답 : {answer}")
#     if answer == result:
#         print(f"case {i} 정답")
#     else:
#         print(f"case {i} 땡!")
#     print()