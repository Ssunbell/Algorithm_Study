iter = int(input())

for i in range(iter):
    dup, text = input().split()
    space = []
    for j in range(len(text)):
        txt = list(text)[j] * int(dup)
        space.append(txt)
    print(''.join(space))