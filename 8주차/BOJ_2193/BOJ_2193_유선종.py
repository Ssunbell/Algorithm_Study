# n = int(input())
# dp = [0, 1, 2] + [0]* (n-1)

# for i in range(3, n + 1):
#     dp[i] = dp[i-2] + dp[i-1]

# print(dp[n])

# 메모리 오류 남

n = int(input())

pinary = [[],[]]

for i in range(1, n + 1):
    if i == 1:
        pinary[i].append([1])
    
    else:
        pinary.append([])
    for tree in pinary[i-1]:
        if tree[-1] != 1:
            pinary[i].append(tree + [1])
            pinary[i].append(tree + [0])
        else:
            pinary[i].append(tree + [0])
print(len(pinary[i]))

'''
[[[]], [[1]], [[1,0]], [[1,0,1],[1,0,0]], [[1,0,1,0], [1,0,0,0], [1,0,0,1]]]
1 2 3 4 5 6 7
1 1 2 3 5 8 13
'''