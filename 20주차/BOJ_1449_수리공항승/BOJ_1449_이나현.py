#[수리공 항승]
N, L = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()
tape = hole[0] #테이프의 왼쪽 끝
cnt = 1
for h in hole:
    if h >= tape + L: #테이프가 안닿을 위치에 구멍이 있을 때
        tape = h
        cnt += 1
print(cnt)