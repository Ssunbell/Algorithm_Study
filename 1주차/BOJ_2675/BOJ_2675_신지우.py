T = int(input())

for i in range(T):
    S, R = input().split()
    S = int(S)
    for j in R:
        P = j * S
        print(P, end="")
    print()
