word_list = [list(input()) for i in range(5)]

word = ""
for i in range(15):
    for j in range(5):
        if len(word_list[j]) > i:
            word += word_list[j][i]

print(word)
