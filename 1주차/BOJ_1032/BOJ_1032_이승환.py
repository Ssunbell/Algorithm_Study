num = int(input())
dir = list(input() for i in range(num))

result = ""
if num < 2:
    print(dir[0])
else:
    for i in range(len(dir[0])):
        for j in range(1, num):
            if dir[j-1][i] == dir[j][i]:
                word = dir[0][i]
            else:
                word = "?"
                break
        result += word

print(result)
