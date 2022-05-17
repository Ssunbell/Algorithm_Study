import sys

input = lambda : sys.stdin.readline().strip()

expression = input()

# 숫자만 뽑아내기
temp = expression.replace('+', '.')
temp = temp.replace('-', '.')
numbers = list(map(int,temp.split('.')))

# 연산 기호만 뽑아내기
plus = expression.count('+') + 1
minus = expression.count('-')
com = plus + minus

nominator = 1
for i in range((plus + 1), com + 1):
    nominator *= i

denominator = 1
for i in range(1, (com - plus)):
    denominator *= i

case_all = int(nominator/denominator)

space = []
for _ in range(case_all):
    switch = case_all
    temp = []
    start = 0
    end = plus
    while switch:
        for i in range(start, case_all-end):
            temp.append(i)
        start += 1
        end -= 1
        switch -= 1
    space.append(temp)

print(space)
        



'''
8개 중에서 +가 5개일 경우
8C5 = (8 * 7 * 6 / 3 * 2 * 1) / 2

'''


answer = 10 ** 10

        