import sys

input_s = lambda : sys.stdin.readline().strip()

n,m = map(int,input_s().split())
ice = [list(map(int,input_s().split())) for _ in range(n)]

def year_after(list_,n,m):
    for i in range(n):
        for j in range(m):
            
