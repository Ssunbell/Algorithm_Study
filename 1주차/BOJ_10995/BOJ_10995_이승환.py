n = int(input())

for j in range(n):
    if j % 2 == 1:
        print(" *"*n,end="")
    else:
        print("* "*n,end="")
    print()
