def converter(string):
    _, time, duration = string.split()
    h, m, s = map(float, time.split(":"))
    microsec, duration = int(3600000*h + 60000*m + 1000*s), int(1000*float(duration[:-1]))
    return microsec-duration+1, microsec

def solution(lines):
    queries = [converter(i) for i in lines]
    available_times = sum([[(s-999, idx), (e, idx)] for idx, (s,e) in enumerate(queries)],[])
    answer = 0
    for s_time, s_idx in sorted(available_times):
        cnt = 0
        for task_init, task_end in queries[s_idx:]:
            if task_init > s_time+999: continue
            elif task_end < s_time: continue
            else: cnt += 1
        answer = max(answer, cnt)
    return answer

"""
converter : line을 마이크로 단위의 (시작시간, 끝나는시간) 으로 반환
1. lines을 시간으로 변환
2. 처리시간은 시작시간 혹은 끝시간을 포함해야 함.
    시작시간의 초기 부분(s-999)을 포함하거나, 끝시간의 마지막 부분을 포함하는(e) 시간들을 미리 저장, idx또한 저장
3. 2에서 구한 처리시간들에 대해서 검사
    3-1. 함께 저장된 idx 번째 인덱스에 있는 쿼리부터 탐색
    3-2. 시간이 겹치지 않으면 continue
    3-3. 시간이 겹치면 cnt += 1
4. answer 갱신
"""