import sys

input_s = lambda : sys.stdin.readline().strip()

t = int(input_s())

for _ in range(t):
    num_tong = int(input_s())
    tong = list(map(int,input_s().split()))
    tong.sort()
    result = [0] * num_tong
    # 각 통나무의 난이도 차가 작으려면
    # 가장 작은 통나무에서 천천히 올라가서
    # 가장 큰 통나무에서 천천히 내려온다.
    # 가장 작은 통나무를 하나씩 결과의 양 끝단에 배치한다.
    idx = 0
    for l in tong:
        result[idx] = l
        if idx == abs(idx):
            idx += 1
            idx = -idx
        else:
            idx = abs(idx)
    max_diff = 0
    for i in range(1,num_tong):
        diff = abs(result[i] - result[i-1])
        max_diff = max(diff,max_diff)
    
    print(max_diff)