import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]

toggle_cnt = 0
# 좌측 상단은 (i, j)
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            # 좌측 상단값이 다르면 해당 좌표를 기준으로 3x3 행렬을 toggle
            for q in range(3):
                for w in range(3):
                    a[i + q][j + w] = a[i + q][j + w] ^ 1
            toggle_cnt += 1
if a == b:
    print(toggle_cnt)
else:
    print(-1)

'''
n과 m 모두 50 이하의 자연수이므로 최대 (50 - 3)^2 * 3^2 = 20000으로, 모든 좌표에 검사를 진행해도 문제 없을거라 생각했다.
또한, 기준점에서 시작하여 조건에 맞지 않는다면 toggle하는 과정을 거치면 이 후 해당 좌표는 연산에서 더이상 고려할 필요가 없다고 생각하여 Greedy 알고리즘을 사용했다.

좌측 상단부터 시작하여 모든 좌표를 확인하고 다르면 해당 좌표를 좌상단으로 하는 3x3 행렬을 toggle한다.
이러한 과정으로 같아질 수 없는 칸이 있다면 불가능으로 간주한다.
'''
