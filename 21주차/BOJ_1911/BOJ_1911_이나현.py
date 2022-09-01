#[흙길 보수하기] -> 시간초과
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0], x[1]))
start = arr[0][0] #널빤지 왼쪽끝
cnt = 1
for i in range(N):
    if arr[i][0] > start + L:
        start = arr[i][0]
        cnt += 1
    cnt += (arr[i][1] - start)//L - 1
    start += ((arr[i][1] - start)//L - 1) * L
    if arr[i][1] > start + L:
        cnt += 1
        start += L
print(cnt)

# 13, 14줄에서 -1이 있는 이유 : 
#   arr[i] = (100, 300), L = 10, start = 100일 때,
#   cnt는 20개면 되는데, 위에서 이미 cnt += 1을 했기 때문
#   start는 290이면 됨, 300까지 갈 필요 x

# 15줄 ~ 17줄
# 위의 주석 예시 경우에서 arr[i][1] = 301 인 경우 널빤지 하나 더 필요