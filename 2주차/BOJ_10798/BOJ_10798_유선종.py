storage = [list(''.join(input())) for i in range(5)]
text_len = [len(storage[i]) for i in range(5)]
max_text = max(text_len)

line = []
for i in range(max_text):
    for j in range(5):
        if i < len(storage[j]):
            line.append(storage[j][i])

print(''.join(line))