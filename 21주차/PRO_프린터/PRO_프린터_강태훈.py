from collections import deque
def solution(priorities, location):
    task = deque(enumerate(priorities))
    answer = 0
    while task:
        curr = task.popleft()
        if task and max(list(zip(*task))[1]) > curr[1]:
            task.append(curr)
        else:
            answer += 1
            if curr[0] == location:
                return answer

testcase = [[[2,1,3,2],2],[[1,1,9,1,1,1],0],[[1,1,2,3,2,1],0]]
for printlist, idx in testcase:
  print(solution(printlist, idx))