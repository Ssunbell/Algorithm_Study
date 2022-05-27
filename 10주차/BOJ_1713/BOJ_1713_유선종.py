import sys

input = lambda : sys.stdin.readline().strip()

n, m = int(input()), int(input())
student = list(map(int, input().split()))

frame = [0] * n # 후보명
order = [0] * n # 순서
vote = [0] * n # 횟수

for i, candidate in enumerate(student):
    if candidate in frame: # 프레임에 해당 후보가 있는 경우
        idx = frame.index(candidate)
        vote[idx] += 1
        
    else: # 프레임에 해당 후보가 없는 경우에
        if 0 in frame: # 프레임이 아직 비어있는 경우
            idx = frame.index(0)
            frame[idx] = candidate
            order[idx] = i
            vote[idx] = 1
            
        else:
            out = min(vote)
            if vote.count(out) > 1: # 해당 후보가 두명 이상
                min_order = 1001
                for idx, cnt in enumerate(vote):
                    if cnt == out:
                        min_order = min(min_order, order[idx])
                idx = order.index(min_order)
                
            elif vote.count(out) == 1: # 해당 후보가 한명만
                idx = vote.index(out)
            frame[idx] = candidate
            order[idx] = i
            vote[idx] = 1

result = [num for num in frame if num != 0]
print(*sorted(result))