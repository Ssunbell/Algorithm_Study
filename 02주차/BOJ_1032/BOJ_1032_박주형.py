n = int(input())
file1, others = input(), [input() for _ in range(n - 1)]
pattern = ""

for i, char in enumerate(file1):
    for other in others:
        if char != other[i]:
            pattern += "?"
            break
    else:
        pattern += char
print(pattern)
