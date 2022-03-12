n = int(input())
if n == 1:
    print(input())
else:
    space = [list(input()) for i in range(n)]
    print(space)
    text_len = len(space[0])
    print(text_len)
    total = []
    for col in range(text_len):
        intersection = set([space[row][col] for row in range(n)])
        if len(intersection) > 1:
            total.append('?')
        else:
            total.append(space[0][col])
    print(''.join(total))