N = int(input())

counseling = [list(map(int,input().split())) for _ in range(N)]

# 각 일차별 상담을 했을 시 상담 가능한 모든 날 구학.
counsel_day_aff = []

for j in range(N):
    if counseling[j][0] <= N-j: # N+1일에 회사에 없어서 상담을 못하는 상담일정을 제외
        no_cp = j + counseling[j][0] # j일차에 상담일 + j = 이날까지 상담 불가능
        cd = []
        cd.append(j)
        for i in range(j+1,N):
            if i >= no_cp and counseling[i][0] <= N-i: # 상담불가기간이 아니고 회사에있는날
                cd.append(i)
                no_cp = i + counseling[i][0] # 새로운 상담불가기간 생성
        counsel_day_aff.append(cd)

sal = []
for i in counsel_day_aff:
    sum = 0
    for j in i:
        sum += counseling[j][1]
    sal.append(sum)

print(max(sal))

