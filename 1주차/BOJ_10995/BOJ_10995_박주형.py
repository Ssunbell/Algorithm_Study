n = int(input())

for i in range(n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print(" *" * n)


n = int(input())
line = "* " * n

for i in range(n):
    print(line)
    line = line[::-1]
    