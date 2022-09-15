#[프로그래머스_주차요금계산]
import math

def solution(fees, records):
    latest = dict()
    times = dict()
    #차들이 머무른 시간 계산
    for record in records:
        time, num, IO = record.split()
        time = 60*int(time[:2]) + int(time[3:])
        num = int(num)
        if num not in latest:        #새로운 차 등록
            latest[num] = [time, IO] #각 차에 대한 최신정보
            times[num] = 0           #각 차에 대한 주차된 시간
        if IO == 'OUT':
            times[num] += time - latest[num][0]
        latest[num] = [time, IO]
    
    #각 차에 대해 요금정산
    answer = []
    nums = sorted(latest.keys())
    for n in nums:
        if latest[n][1] == 'IN':     #자정이 되어도 안나간 차
            times[n] += (23*60 + 59) - latest[n][0]
        if times[n] <= fees[0]:      #머무른 시간이 기본시간 이내
            answer.append(fees[1])
        else:                        #기본시간 초과
            fare = fees[1] + math.ceil((times[n]-fees[0]) / fees[2]) * fees[3]
            answer.append(fare)
    return answer