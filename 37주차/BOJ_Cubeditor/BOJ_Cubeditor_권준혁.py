def make_table(s):
    j = 0
    table = [0] * len(s)
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = table[j - 1]
        if s[i] == s[j]:
            j += 1
            table[i] = j
    return table

if __name__ == '__main__':
    s = input()
    answer = 0
    for i in range(len(s)):
        answer = max(answer, max(make_table(s[i:])))
    print(answer)