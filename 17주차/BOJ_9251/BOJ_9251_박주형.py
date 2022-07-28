import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
h, w = len(word1), len(word2)
c = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word1[i-1] == word2[j-1]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i][j-1], c[i-1][j])
print(c[-1][-1])