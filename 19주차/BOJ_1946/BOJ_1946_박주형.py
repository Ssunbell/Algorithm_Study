import sys


input = sys.stdin.readline


n = int(input())

for _ in range(n):
    m = int(input())
    applicant = []
    for _ in range(m):
        x, y = map(int, input().split())
        applicant.append([x, y])
    applicant.sort()
    applicant_rank = applicant[0][1]
    cnt = m
    for i in range(1, m):
        if applicant_rank < applicant[i][1]:
            cnt -= 1
        else:
            applicant_rank = applicant[i][1]
    print(cnt)
print()
