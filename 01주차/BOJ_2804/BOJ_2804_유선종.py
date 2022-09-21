a, b = input().split()
storage = []

for i in b:
    if a.find(i) > -1:
        storage.append(a.find(i))

col = min(storage)
row = b.find(a[col])

for i, b_char in enumerate(b):
    if i == row:
        print(a)
    else:
        print('.'*col + b_char + '.'*(len(a)-col-1))
        