# p(i)를 i일차의 상담기간, s(i)를 i일차에 상담을 할 경우 얻는 수익이라 할 때,
# 상담이 끝나는 날짜는 i+p(i)-1, i+p(i)일차부터는 상담 가능
# 만약 i+p(i)-1 > N 이면 회사에 없기때문에 상담이 불가능이므로 수익은 0
# i+1,i+2...i+p(i)-1일차까지는 i일차에 상담을 진행하면 상담을 못함.
# i일차에 상담을 하면 i+p(i)일차부터 상담 가능
# income(i)는 i일차부터 상담을 시작했을 때 얻을수 있는 최대 수익
# income(i) = s(i) + max(income(i+p(i)), income(i+(p(i)+1), ...,income(N))

N = int(input())

s = [list(map(int, input().split())) for _ in range(N)]
# 날짜 계산의 용이성을 위해 더미 추가
dummy = [[0, 0]]
schedule = dummy + s

# 일차별 수익을 저장할 리스트
# i+p까지 비교해야하므로 p의 최대값인 5을 더함
income = [0 for _ in range(N+5)]

for i in range(N, 0, -1):
    if schedule[i][0] + i - 1 > N:
        income[i] = 0
    else:
        income[i] = schedule[i][1] + max(income[i+schedule[i][0]:])

print(max(income))
