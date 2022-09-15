#[배]
import sys
input = sys.stdin.readline

N = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse=True)
if boxes[0] > cranes[0]: #모든 크레인 무게제한보다 더 큰 무게의 박스가 있으면
    print(-1)
else:
    answer = 0
    while True:
        if len(boxes) == 0:
            break
        answer += 1
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
    print(answer)