import math
from collections import defaultdict


def solution(fees, records):

    def total_fee(t):
        # 주차시간을 입력하면 요금을 계산해주는 함수. 최저요금은 max함수를 사용함
        return fees[1] + math.ceil(max(0, t - fees[0]) / fees[2]) * fees[3]

    # 차량 번호를 key로 해당 차량의 입, 출차 정보를 저장하는 딕셔너리.
    # 문제 조건에서 잘못된 입, 출차 기록이 없었으므로 IN, OUT 정보는 필요없음.
    user_inform = defaultdict(list)
    for record in records:
        time, car, ty = record.split()
        user_inform[car].append(list(map(int, time.split(":"))))

    # 차량 별 이용시간을 저장할 리스트
    use_time_list = []

    # 차량 번호를 기준으로 출력해야 하므로, 입출차 정보가 저장되어 있는 딕셔너리 user_inform의 items를 key순으로 정렬하여 사용
    for carnum, timelist in sorted(user_inform.items()):

        # 입출차 기록의 개수
        iolog = len(timelist)
        # timelist에서 총 사용시간을 계산하여 use_time에 저장
        use_time = 0

        # 차량이 23:59 이후에도 OUT한 기록이 없으면 해당 차량의 timelist 에 [23, 59]를 추가함.
        if iolog % 2 == 1:
            timelist.append([23, 59])
            iolog += 1

        # 리스트 내 원소의 개수는 무조건 짝수. 2개 단위로 자르면 입, 출차 기록임. 출차시간에 입차시간을 빼고 분단위로 바꾸어 use_time에 더함.
        for i in range(0, iolog, 2):
            use_time += 60 * \
                (timelist[i+1][0] - timelist[i][0]) + \
                timelist[i+1][1] - timelist[i][1]
        use_time_list.append(use_time)
    return list(map(total_fee, use_time_list))


test_case = [[[180, 5000, 10, 600],
              ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]],
             [[120, 0, 60, 591],
              ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]],
             [[1, 461, 1, 10],
              ["00:00 1234 IN"]]
             ]

for t, q in test_case:
    print(solution(t, q))

'''
입력받은 records를 차량별로 나누어 딕셔너리에 저장
딕셔너리의 items를 차량번호 기준으로 정렬하고 총 이용시간을 계산하여 저장
total_fee 함수에 이용시간을 입력하여 비용을 출력

IN, OUT 정보가 주어졌지만 잘못된 입출차 정보가 없다는 조건으로 인해 고려할 필요가 없었다. 단, 출차 정보가 없을 경우 23:59 에 출차한걸로 간주하여 총 이용시간을 구한다.
'''
