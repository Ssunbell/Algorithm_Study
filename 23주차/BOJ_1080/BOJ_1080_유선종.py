import sys

input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

cnt = 0
for row in range(N-2):
    for col in range(M-2):
        if A[row][col] != B[row][col]:
            cnt += 1
            for rp in range(3):
                for cp in range(3):
                    if A[row+rp][col+cp] == 0:
                        A[row+rp][col+cp] += 1
                    else:
                        A[row+rp][col+cp] -= 1

if A == B:
    print(cnt)
else:
    print(-1)

'''
3 by 3의 크기로 변경해야되기 때문에 내가 바꾸고 싶지 않아도 바꿔야 하는 값들이 존재
예를 들어, (0,0)을 바꿔줬는데 (1,1)때문에 (0,0)을 또 변경해줘야 한다면 이는 풀 수 없는 문제임
따라서 고정된 값을 기준으로 체크해보고 그래도 두 행렬이 다른 행렬이라면 이건 만들수 없는 행렬
'''