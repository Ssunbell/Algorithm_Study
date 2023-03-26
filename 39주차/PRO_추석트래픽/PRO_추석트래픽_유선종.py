from typing import *
from decimal import Decimal

def float_calculate(a, b):
    return float(Decimal(a) - (Decimal(b) - Decimal('0.001')))

def solution(lines:List[str]) -> int:
    throughput = []
    range_list = []
    for line in lines:
        date, time, range_t = line.split()
        hour, minute, second = time.split(':')
        start_s = int(hour) * 3600 + int(minute) * 60 + float_calculate(second, range_t[:range_t.index('s')])
        end_s = int(hour) * 3600 + int(minute) * 60 + float(second)
        
        throughput.append(start_s)
        throughput.append(end_s)
        range_list.append((start_s, end_s))

    answer = 0
    for t in throughput:
        tmp = 0
        t_e = float(Decimal(str(t)) + Decimal('0.999'))
        for s, e in range_list:
            if (
                t <= s <= t_e or
                t <= e <= t_e or
                s <= t and t_e <= e
            ):
                tmp += 1
        answer = max(answer, tmp)
    return answer