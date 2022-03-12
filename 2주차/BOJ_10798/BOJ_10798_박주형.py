words = [list(map(str, *input().split())) for i in range(5)]
max_len = max(len(word) for word in words)
vertical_words = ""


for k in range(max_len):
    for j in range(5):
        if k < len(words[j]):
            pass
            vertical_words += words[j][k]

print(vertical_words)
