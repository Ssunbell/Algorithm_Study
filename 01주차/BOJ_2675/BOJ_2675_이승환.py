testcase_num = int(input())

for i in range(testcase_num):
    num, s = input().split()
    for j in s:
        print(j * int(num),end="")
    print()