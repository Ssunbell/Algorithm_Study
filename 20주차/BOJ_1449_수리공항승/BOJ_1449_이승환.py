num_tape, len_tape = map(int,input().split())
pipe = list(map(int,input().split()))

pipe = sorted(pipe)

# 첫 테이프를 붙일 자리
start = pipe[0]

# 사용한 테이프의 개수
used_tape = 1

# 처음부터 테이프의 개수 세기
for location in pipe:
    if (start - 0.5) + len_tape < location:
        # 이전 테이프로 물이 새는 곳을 커버하지 못하면 새로 테이프를 붙임
        start = location
        used_tape += 1

print(used_tape)