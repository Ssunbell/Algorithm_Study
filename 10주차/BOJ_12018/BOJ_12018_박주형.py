# 과목당 마일리지를 1 ~ 36 분배
# 과목에 대해 마일리지를 많이 투자한 순으로 수강인원만큼 신청
# 마일리지가 같다면 성준이 우선 (성준이가 마지막으로 신청)
# 우선적으로 마일리지 sort
# 신청자 > 수강인원 : 신청자 - 수강인원 인덱스랑 같은 수 (마일리지 같으면 성준이 우선순위기 때문)
# 신청자 = 수강인원 : 0번 인덱스랑 같은 수
# 신청자 < 수강인원 : 1 (성준이 이후 신청자 없기 때문)
# m에서 마일리지 빼주고 더이상 신청할 수 없을 때 break

n, m = map(int, input().split())
mileages = []
cnt = 0

for _ in range(n):
    p, l = map(int, input().split())
    mil = list(map(int, input().split()))
    mil.sort()
    num = p - l
    if num >= 0:
        mileages.append(mil[num])
    if num < 0:
        mileages.append(1)

mileages.sort()

for mileage in mileages:
    cnt += 1
    m -= mileage
    if m < 0:
        cnt -= 1
        break

print(cnt)

# 30840kb 76ms