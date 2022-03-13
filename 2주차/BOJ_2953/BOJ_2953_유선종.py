score = [sum(map(int, input().split()))for i in range(5)]
max_score = max(score)
print(score.index(max_score)+1, max_score)