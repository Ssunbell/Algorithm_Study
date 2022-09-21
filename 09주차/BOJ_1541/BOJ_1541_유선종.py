import sys

input = lambda : sys.stdin.readline().strip()

expression = input()

temp = expression.split('-')
storage = []
for i in temp:
    numbers = i.split('+')
    plus_num = 0
    for number in numbers:
        plus_num += int(number)
    storage.append(plus_num)

for i, num in enumerate(storage):
    if i == 0:
        answer = num
    else:
        answer -= num

print(answer)

####### 조합을 사용 #########

# # 숫자만 뽑아내기
# temp = expression.replace('+', '.')
# temp = temp.replace('-', '.')
# numbers = list(map(int,temp.split('.')))

# # 연산 기호만 뽑아내기
# plus = expression.count('+') + 1
# minus = expression.count('-')
# com = plus + minus

# nominator = 1
# for i in range((plus + 1), com + 1):
#     nominator *= i

# denominator = 1
# for i in range(1, (com - plus)):
#     denominator *= i

# case_all = int(nominator/denominator)
# '''
# 8개 중에서 +가 5개일 경우
# 8C5 = (8 * 7 * 6 / 3 * 2 * 1)
# '''

# def combination(n, r, c=[], answer = []):
#     if r == 0:
#         answer.append(c)

#     else:
#         for i in range(1, 1+n):
#             if c.count(i) == 0 or i > max(c):
#                 c.append(i)
#                 combination(n, r-1, c)
#                 c.remove(i)
                
# answer = combination(com, plus)
# print(answer)

# answer = 10 ** 10

        