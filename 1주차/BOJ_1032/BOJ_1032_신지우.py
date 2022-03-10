n = int(input())
file_name = list(input())

for i in range(n-1):
    file_names = list(input())
    for j in range(len(file_name)):
        if file_name[j] != file_names[j]:
            file_name[j] = '?'

for i in file_name:
    print(i, end="")