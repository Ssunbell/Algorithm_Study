import sys 

input = lambda:sys.stdin.readline().rstrip()

def back(depth):
    if depth == m:
        print(" ".join(map(str, lst)))
        return

    for i in range(len(arr)):
        if depth == 0 or lst[-1]<=arr[i]:
            lst.append(arr[i])
            back(depth+1)
            lst.pop()

n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

lst = []
back(0)