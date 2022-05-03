import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
data = [int(input()) for _ in range(n)]

def mean(data):
    return int(round(sum(data)/len(data),0))

def median(data):
    data.sort()
    a,b = divmod(len(data),2)
    if b == 1:
        return data[a]
    else:
        return (data[a-1] + data[a]) / 2

def mode(data):
    answer=dict()
    for num in data:
        if num not in answer.keys():
            answer[num]=1
        else: answer[num]+=1
    
    return max(answer, key=answer.get)

def range_st(data):
    return max(data) - min(data)

print(mean(data))
print(median(data))
print(mode(data))
print(range_st(data))