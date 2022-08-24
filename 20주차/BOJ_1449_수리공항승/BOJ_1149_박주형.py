# 5 2
# 1 2 100 101

# 101 100 ..... 2 1
#   1  1
#               2 2   

# 4 3
# 1 2 3 4

# 4 3 2 1
# 1 1 1 
#   2 2 2 

# 5 4
# 1 2 4 5 9

# 9 8 7 6 5 4 3 2 1
# 1 1 1 1
#       2 2 2 2 
#           3 3 3 3


import sys

input = sys.stdin.readline

n, l = map(int, input().split())
pipes = list(map(int, input().split()))
pipes.sort()

cnt = 1
start = pipes[0]

for i in range(len(pipes)):
    if l > pipes[i] - start:
        pass
    else:
        start = pipes[i]
        cnt += 1

print(cnt)
