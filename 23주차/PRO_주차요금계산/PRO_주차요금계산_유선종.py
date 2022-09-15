from math import ceil

def solution(fees, records):
    s = []
    temp = []
    for rows in records:
        time, car_num, check = rows.split()
        hour, min = time.split(':')
        if '0' == hour[0]:
            hour = int(hour[1]) * 60
        else:
            hour = int(hour) * 60
        time = hour + int(min)
        
        if check == 'IN':
            s.append({car_num : time})
        else:
            for i, park in enumerate(s):
                if list(park.items())[0][0] == car_num:
                    tmp = s.pop(i)
                    tmp[car_num] = time - tmp[car_num]
                    temp.append(tmp)
                    
    while s:
        tmp = s.pop(0)
        car_num, time = list(tmp.items())[0]
        temp.append({car_num : (23*60 + 59) - time})
    
    
    result = {}
    for row in temp:
        car_num, time = list(row.items())[0]
        if car_num not in result:
            result[car_num] = time
        else:
            result[car_num] += time
    result = sorted(result.items(), key=lambda x: x[0])
    
    answer = []
    for row in result:
        if row[1] > fees[0]:
            answer.append(fees[1] + ceil(((row[1] - fees[0]) / fees[2])) * fees[3])
        else:
            answer.append(fees[1])

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))

