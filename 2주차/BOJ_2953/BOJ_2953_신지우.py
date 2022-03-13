total_list = []

for i in range(5):
    A, B, C, D = map(int, input().split())
    total = A + B + C + D
    total_list.append(total)

win = max(total_list)
print(total_list.index(win) + 1, win)