h, w, x, y = map(int, input().split())

A = [[] for i in range(h)]
B = [list(map(int,input().split())) for j in range(h+x)]

# 행은 h, 열은 w
# A를 x만큼 행을 이동시키고 y만큼 열을 이동시킴
# 즉, h,w 만큼의 반복에서 i < x 이면 원래 A와 같음.
# i >= x 이면 행만큼 이동한 A
# j >= y 이면 A[i][j] + A[i-x][j-y]
# 만약 i >= x 인데 j < y 이면 A[i][j] = B[i][j]

for i in range(h):
    for j in range(w):
        if i<x :
            A[i].append(B[i][j])
        else :
            if j >= y:
                A[i].append(B[i][j] - A[i-x][j-y])
            else:
                A[i].append(B[i][j])

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j],end=" ")
    print()
