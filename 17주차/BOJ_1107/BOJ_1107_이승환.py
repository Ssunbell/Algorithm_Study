channel = int(input())
borken_num = int(input())

if borken_num == 0:
    borken_button = []
else:
    borken_button = list(map(int,input().split()))

min_button = abs(100 - channel)

for i in range(1000000):
    for b in str(i):
        if int(b) in borken_button:
            break
    else:
        min_button = min(min_button, len(str(i)) + abs(channel-i))
    

print(min_button)