s = input()
for i in range(1, len(s)):
    for j in range(0, i):
        tmp = s[j:len(s) - i + j]
        if tmp in s[j + 1:]:
            print(len(tmp))
            exit(0)
else:
    print(0)