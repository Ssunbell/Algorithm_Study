case_num = int(input())

for i in range(case_num):
    index, text = input().split()
    print(text[:int(index)-1] + text[int(index):])