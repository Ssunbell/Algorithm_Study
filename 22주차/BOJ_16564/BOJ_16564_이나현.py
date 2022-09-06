#[히오스 프로그래머]
import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
char = [int(input()) for _ in range(N)]
start = min(char)
end = max(char) + K
while start <= end:
    mid = (start+end) // 2
    x = 0 # x는 모든 캐릭터의 레벨이 최소 mid레벨이 되기 위해 필요한 레벨의 총합
    for level in char:
        x += max(0, mid - level)
    if x > K: # mid가 되기위해 K보다 더 많은 레벨 필요 -> mid보다 더 작은 구간 탐색
        end = mid - 1
    else: # x <= K
        start = mid + 1
        answer = mid
print(answer)