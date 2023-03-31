# 프로그래머스_추석트래픽
# 시간은 밀리초로 모두 변환하여 계산
# 요청이 끝나는 시간에서 시작하는 1초짜리 구간을 잡는다.
# 그 구간에 대해 모든 요청을 조건 따져가며 확인한다. => 시간복잡도 : O(N^2)

def cal_start_end_time(end_time, interval):
    # end_time을 밀리초로 변환
    hh, mm, ss = end_time.split(':')
    ss, sss = ss.split('.')
    hh, mm, ss, sss = map(int, (hh, mm, ss, sss))
    end_time = (hh * 3600 + mm * 60 + ss) * 1000
    end_time += sss
    # interval 시간 밀리초로 변환
    try:
        ss, sss = map(int, interval[:-1].split('.'))
        interval = ss * 1000 + sss - 1 #-1은 처리시간이 시작시간과 끝시간을 포함하기 떄문(예제 2참고)
    except:
        ss = int(interval[:-1])
        interval = ss * 1000 - 1
    # 시작 시각 계산
    start_time = end_time - interval
    return (start_time, end_time)

def solution(lines):
    requests = []
    for request in lines:
        _, end_time, interval = request.split()
        requests.append(cal_start_end_time(end_time, interval))

    answer = 0
    for _, s in requests:
        e = s + 999
        cnt = 0
        for rs, re in requests:
            if (rs <= s and re >= s) or s <= rs <= e:
                cnt += 1
        answer = max(answer, cnt)
    return answer

# print(solution(["2016-09-15 00:00:00.000 3s"]))
# print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution((["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])))
# print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
# print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))