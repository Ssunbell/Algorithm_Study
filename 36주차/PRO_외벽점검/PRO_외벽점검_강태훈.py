from itertools import permutations
from bisect import bisect_right
from collections import deque

def solution(n, weak, dist):
    answer = 9
    for workers in permutations(dist):
        for s_idx in range(len(weak)):
            front = deque(weak[:])
            back = deque()
            for _ in range(s_idx): back.append(front.popleft())

            for idx, worker in enumerate(workers):
                if front:
                    s = front[0]
                    e = s + worker
                    f_insert_idx = bisect_right(front, e)
                    for _ in range(f_insert_idx):
                        front.popleft()
                    if not front:
                        back_size = e - n
                        if back_size >= 0:
                            b_insert_idx = bisect_right(back, back_size)
                            for _ in range(b_insert_idx):
                                back.popleft()
                elif back:
                    s = back[0]
                    e = s + worker
                    b_insert_idx = bisect_right(back, e)
                    for _ in range(b_insert_idx):
                        back.popleft()

                if (not front) and (not back):
                    answer = min(answer, idx+1)
                    break
    return -1 if answer == 9 else answer

if __name__ == "__main__":
    tc = [
        [12,	[1, 5, 6, 10],	[1, 2, 3, 4],	2],
        [12,	[1, 3, 4, 9, 10],	[3, 5, 7],	1]
    ]
    for n, weak, dist, result in tc:
        print(solution(n, weak, dist), result)