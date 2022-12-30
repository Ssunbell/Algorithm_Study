#[프로그래머스_무지의먹방라이브]
# 효율성 2번 통과 못했습니다.
# step1.먼저 이분탐색으로 몇바퀴를 돌렸는지 확인한다.
#       경과시간이 k와 동일하거나 k보다 살짝 작은 바퀴수를 구한다.
# step2.찾은 바퀴에서 인덱싱 접근으로 정답을 찾는다.

def solution(foods, k):
    s, e = 0, max(foods) #최대 바퀴수는 음식의 최댓값이다.
    len_foods = len(foods)
    if k >= sum(foods):
        return -1

    while s <= e:
        m = (s+e)//2
        
        after_turning_m = [x - m for x in foods]
        minus_arr = [min(x, 0) for x in after_turning_m]
        elapsed_time = m * len(foods) + sum(minus_arr)
        left = [x > 0 for x in after_turning_m] #음식이 남았다면 True, 없다면 False
        if elapsed_time > k: #m바퀴돌렸을 때 k초보다 더 많은 시간이 지났다.
            e = m - 1
        elif k - elapsed_time < sum(left): #m바퀴돌렸을 때, 남은 음식개수보다 작은 수만큼 (k보다) 부족한 초가 지났다.
            break
        else: #너무 적은 바퀴 수
            s = m + 1
    
    index = 0
    while elapsed_time < k:
        while left[index] == False:
            index += 1
        elapsed_time += 1
        index = (index + 1) % len(foods)
    while left[index] == False: #다음 음식의 인덱스 찾기
        index = index + 1
    return index + 1

print(solution([4,2,3,6,7,1,5,8], 27))
print(solution([10,5,7,4], 20))
print(solution(	[3, 1, 2], 5))