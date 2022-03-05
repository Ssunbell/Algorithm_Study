cand = [sum(list(map(int, input().split()))) for i in range(5)]

max_score = max(cand)
max_idx = cand.index(max_score)

print(max_idx+1, max_score)
