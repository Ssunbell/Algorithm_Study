import sys

input = lambda : sys.stdin.readline().strip()
n, m = map(int, input().split())
lecture = []
for _ in range(n):
    p, l = map(int, input().split())
    temp = list(map(int, input().split()))
    temp = sorted(temp, reverse=True)
    lecture.append({p - l : temp[:l]})
print(lecture)

mileage = [0] * n
for i, lct in enumerate(lecture):
    for key, value in lct.items():
        if key < 0:
            mileage[i] = 1
        else:
            mileage[i] = min(value)
            
mileage.sort()
answer = 0
for num in mileage:
    m -= num
    if m < 0:
        m += num
        break
    answer += 1
    

print(answer)
