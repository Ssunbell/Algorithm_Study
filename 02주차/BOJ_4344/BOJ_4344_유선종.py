c = int(input())
storage = []

for i in range(c):
    storage.append(list(map(int, input().split()))[1:])
    
for score_storage in storage:
    average = sum(score_storage)/len(score_storage)
    num = 0
    for score in score_storage:
        if score > average:
            num += 1
    print(f'{num/len(score_storage)*100:.3f}%')