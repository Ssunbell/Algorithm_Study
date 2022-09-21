import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort() # 오름차순

def mean(data):
    return int(round(sum(data)/n,0))

def median(data):
    a,b = divmod(n,2)
    if b == 1:
        return data[a]
    else:
        return (data[a-1] + data[a]) / 2

def mode(data):
    temp = set(data)
    answer = dict()
    for key in temp:
        answer[key] = 0
        
    for num in data:
        answer[num] += 1
        
    max_value = max(answer.values())
    max_list = [key for key, value in answer.items() if value == max_value]
    max_list.sort()
    
    if len(max_list) == 1:
        return max_list[0]
    else:
        return max_list[1]

def range_st(data):
    return data[-1] - data[0]

print(mean(data))
print(median(data))
print(mode(data))
print(range_st(data))