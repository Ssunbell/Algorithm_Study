## === idea ===
## 슬라이드 윈도우가 지나가면서 윈도우 내의 최댓값을 뽑아냄
## 이때, max 함수의 시간복잡도가 높아 시간초과가 나기 때문에
## 최대힙큐를 사용하여 max의 시간복잡도를 줄여줌
from heapq import heappush, heappop

def solution(stones, k):
    hq = []
    answer = 200000000

    for i in range(k - 1):
        heappush(hq, [-stones[i], i])

    ## idx는 슬라이드 가장 마지막 원소를 의미
    for i in range(k - 1, len(stones)):
        heappush(hq, [-stones[i], i])
        
        ## 슬라이드를 벗어나는 구간의 값들은 삭제
        while hq[0][1] < i - k + 1:
            heappop(hq)
            
        ## 슬라이드 구간의 최댓값 중에서 최솟값 저장
        answer = min(answer, -hq[0][0])

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))