N = int(input())
line = list(input())

for i in range(N-1):
    other = input()
    print(other)
    for j in range(len(line)):
        if line[j] != other[j]:
            line[j] ='?'
print(''.join(line))