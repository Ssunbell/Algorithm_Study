import sys
input = sys.stdin.readline
n = int(input())
nums = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
# 음수는 음수끼리 곱하거나 0과 곱해서 처리
while len(nums) > 1 and nums[-1] < 0:
    if nums[-2] <= 0:
        n1, n2 = nums.pop(), nums.pop()
        answer += n1*n2
    else:
        answer += nums.pop()
        break
# 0이나 1은 바로 정답에 더함
while nums and nums[-1] in (0, 1):
    answer += nums.pop()
# 나머지는 큰 수부터 차례대로 묶어서 계산
if len(nums) % 2 == 1:
    answer += nums.pop()
for i in range(0, len(nums), 2):
    answer += nums[i] * nums[i+1]
print(answer)
