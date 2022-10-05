#[도서관]
N, M = map(int, input().split())
loc = list(map(int, input().split())) + [0]
loc.sort()
#책위치 음수리스트, 양수리스트로 나누기
zero_loc = loc.index(0)
negative = loc[:zero_loc]
negative = list(map(lambda x:-x, negative))
positive = sorted(loc[zero_loc+1:], reverse=True)
nega_len = zero_loc
pos_len = N - zero_loc

#절대값이 큰 값들부터 연산
move = 0
for i in range(0,nega_len,M):
    move += negative[i] * 2
for i in range(0,pos_len,M):
    move += positive[i] * 2
#가장 먼 거리를 마지막에 다녀온다고 했다고 가정 -> 돌아올 필요 없음
move -= max(loc[0] * -1, loc[-1])
print(move)