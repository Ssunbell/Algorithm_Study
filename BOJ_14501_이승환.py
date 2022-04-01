# 우선 회사에 없어서 상담을 하지 못하는 경우는 수익을 0으로 계산
# p을 i일차의 상담기간이라고 할 경우
# i+p, i+p+1, i+p+2.... N일차 까지의 수익 중 가장 큰 수익을 선택
# i일차의 최대 수익 = i일차의 수익 + i일차의 상담기간 이후 수익중 최대수익

N = int(input())

s = [list(map(int,input().split())) for _ in range(N)]
# 날짜 계산의 용이성을 위해 더미 추가
dummy = [[0,0]]
schedule = dummy + s

# 처음에는 N+1로 길이를 설정했는데, 런타임에러발생,
# 이유는 상담일자가 최대 5일이고, i와 i+p를 비교해야하기때문.
# 즉, N+5까지 비교할 수 있기 때문에 N+5로 설정해야함.
# vscode상으로는 문제가 없었지만 백준 내부에서 오류가 있는듯.
income = [0 for _ in range(N+5)]

for i in range(N,0,-1):
    if schedule[i][0] > N+1-i:
        income[i] = 0
    else:
        income[i] = schedule[i][1] + max(income[i+schedule[i][0]:])

print(max(income))