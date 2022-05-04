n = int(input())
p = sorted(list(map(int, input().split())))

min_time = 0
sum = 0

for i in p:
    sum += i
    min_time += sum
    
print(min_time)
