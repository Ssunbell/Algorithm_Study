N = int(input())
arr = [int(input()) for _ in range(N)]
#양수리스트, 음수리스트 선언 및 값 추가
positive = []
negative = []
sum = 0
for num in arr:
    if num > 1:
        positive.append(num)
    elif num == 1: #1의 경우 무조건 덧셈 연산
        sum += 1
    else:
        negative.append(num)
positive.sort(reverse=True)
negative.sort()
#홀수개의 리스트의 경우 짝수개로 맞춰주기 위해 끝에 1로 패딩
if len(positive) % 2:
    positive.append(1)
if len(negative) % 2:
    negative.append(1)
#2개씩 묶은 후 덧셈 연산
for i in range(0, len(positive), 2):
    sum += positive[i] * positive[i+1]
for i in range(0, len(negative), 2):
    sum += negative[i] * negative[i+1]

print(sum)