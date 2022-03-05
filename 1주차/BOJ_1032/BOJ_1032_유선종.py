n = int(input())
if n == 1:
    print(input())
else:
    space = [input() for i in range(n)]
    for i, text in enumerate(space):
        for j, text2 in enumerate(space):
            if i < j:
                for k in range(len(text)):
                    if text[k] != text2[k]:
                        text[k] = '?'
                        