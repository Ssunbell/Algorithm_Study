import sys
input = lambda: sys.stdin.readline().strip()

t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    cases.append([tuple(map(int, input().split())) for _ in range(n)])

for case in cases:
    tmp = sorted(case, key=lambda x: (x[0], x[1])) # 서류 기준으로 정렬하면 이제 서류를 비교하지 않아도 됨
    num = 1
    compare = tmp[0][1]
    for score in tmp[1:]: # 면접만 비교
        if score[1] < compare:
            num += 1
            compare = score[1]

    print(num)

# 틀린 이유: 서류 정렬과 면접 정렬을 함으로써 두번 비교했고, 이는 동시에 비교하는 것이 아님. 따라서 동시에 비교할 수 있는 위의 방식대로 해야 함
'''
for case in cases:
    tmp1 = sorted(case, key=lambda x: (x[0], x[1])) 
    result1 = [tmp1[i] for i in range(1, len(tmp1)) if tmp1[i][0] > tmp1[i-1][0] and tmp1[i][1] > tmp1[i-1][1]]
    tmp2 = sorted(case, key=lambda x: (x[1], x[0]))
    result2 = [tmp2[i] for i in range(1, len(tmp2)) if tmp2[i][0] > tmp2[i-1][0] and tmp2[i][1] > tmp2[i-1][1]]
    result = set(result1 + result2)

    print(result)
    print(len(tmp1) - len(result))
'''