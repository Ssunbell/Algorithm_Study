wood = list(map(int, input().split()))

switch = 1
while switch:
    for i in range(4):
        if wood[i] > wood[i+1]:
            wood[i : i+2] = [wood[i+1], wood[i]]
            print(' '.join(map(str,wood)))
    if wood == [1,2,3,4,5]:
        switch = 0