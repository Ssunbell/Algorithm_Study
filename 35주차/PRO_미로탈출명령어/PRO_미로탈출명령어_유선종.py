import sys
sys.setrecursionlimit(10**6)

def solution(n, m, x, y, r, c, k):
    if (
        x == r and # row
        y == c and # col
        k == 0 # steps
    ):  return '' # 모든 발걸음을 소모하여 도착 지점에 도착

    d = abs(x - r) + abs(y - c) # distance
    
    if d > k or d % 2 != k % 2: # 거리가 step보다 크거나 둘다 짝수 or 홀수가 아닌 경우
        return 'impossible'

    if d == k: # 거리가 같다면 최적의 거리로 도착해야 함 -> 기준은 도착지점
        if x < r: # 도착지점보다 위에 있을 경우
            return 'd'+solution(n,m,x+1,y,r,c,k-1)
        elif y > c: # 도착 지점보다 오른쪽에 있을 경우
            return 'l'+solution(n,m,x,y-1,r,c,k-1)
        elif y < c: # 도착 지점보다 왼쪽에 있을 경우
            return 'r'+solution(n,m,x,y+1,r,c,k-1)
        elif x > r: # 도착 지점보다 아래에 있을 경우
            return 'u'+solution(n,m,x-1,y,r,c,k-1)
    elif k > d: # 거리보다 더 많은 steps을 가야 하므로 낭비되는 steps 존재 -> 기준은 맵
        if x < n:
            return 'd'+solution(n,m,x+1,y,r,c,k-1)
        elif y > 1:
            return 'l'+solution(n,m,x,y-1,r,c,k-1)
        elif y < m:
            return 'r'+solution(n,m,x,y+1,r,c,k-1)
        elif x > 1:
            return 'u'+solution(n,m,x-1,y,r,c,k-1)