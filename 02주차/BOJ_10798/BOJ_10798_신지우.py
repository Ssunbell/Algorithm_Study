word = [input() for i in range(5)]
print(word)
word_max = max(len(i) for i in word)

for i in range(word_max):
    for j in word:
        if i < len(j):
            print(j[i], end='')