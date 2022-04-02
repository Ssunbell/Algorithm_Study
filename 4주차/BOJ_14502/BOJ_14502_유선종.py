import copy
n, m = map(int, input().split())

def locate(list_name, index_1, num):
    n = -1
    result = []
    while True:
        if list_name[n+1:].count(num) == 0:
            break
        n += list_name[n+1:].index(num) + 1
        result.append([index_1, n])
    return result

virus_start = []
null_location = []
lab = []
two_len = 0
one_len = 0

for i in range(n):
    temp = list(map(int, input().split()))
    two_len += temp.count(2)
    one_len += temp.count(1)
    lab.append(temp)
    temp_virus = locate(temp, i, 2)
    temp_null = locate(temp, i, 0)
    if temp_virus:
        virus_start.append(temp_virus)
    if temp_null:
        null_location.append(temp_null)

virus_start = sum(virus_start, [])
null_location = sum(null_location, [])
com = len(null_location)


null_space = []
for i in range(com - 2):
    for j in range(i + 1, com - 1):
        for z in range(j + 1, com):
            null_space.append([null_location[i]] + [null_location[j]] + [null_location[z]])    
            
###################################################

def dfs(row, col):
    if row < 0 or col < 0 or row >= n or col>= m:
        return 

    if graph[row][col] == 0:
        graph[row][col] = 2
        
        dfs(row-1, col)
        dfs(row, col - 1)
        dfs(row + 1, col)
        dfs(row, col + 1)
        return 
    
    elif graph[row][col] == 1 or graph[row][col] == 2:
        return 



if one_len + 3 >= two_len:
    result = 0
    for wall in null_space:
        graph = copy.deepcopy(lab)
        graph[wall[0][0]][wall[0][1]] = 1
        graph[wall[1][0]][wall[1][1]] = 1
        graph[wall[2][0]][wall[2][1]] = 1
        
        for matrix in virus_start:
            dfs(matrix[0], matrix[1])
            null_count = sum(graph,[]).count(0)
            if result < null_count:
                result = null_count
    print(result)
else:
    result = 0
    for wall in null_space:
        graph = copy.deepcopy(lab)
        graph[wall[0][0]][wall[0][1]] = 1
        graph[wall[1][0]][wall[1][1]] = 1
        graph[wall[2][0]][wall[2][1]] = 1
        
        for matrix in virus_start[0]:
            dfs(matrix[0], matrix[1])
            null_count = sum(graph,[]).count(0)
            if result < null_count:
                result = null_count
    print(result)

'''
아이디어

1. 1이 2보다 많거나 같다면 물을 막을 둑이 있으므로
물길을 막아 물이 넘치지 않도록 차단한다.
 - 먼저 1을 넣어서 둑을 쌓아본다.
 - 2의 갯수를 늘리면서 물이 어떤 물길을 따라 흐르는지 파악한다.
 - 이 과정을 반복하여 최대한 0을 살리는 방법을 채택한다.
 

2. 2가 1보다 더 많다는 것은 강이 범람하는 것을 막을 수 없으므로
내 한몸 살리기 위해 물을 막는 것이 아닌 건물 위로 올라간다.
 - 2의 갯수를 늘리면서 홍수가 일어나는 과정을 구현할 필요가 없다.
   어짜피 물에 잠긴다.
 - 따라서 가지고 있는 1을 이용하여 최대한의 공간을 확보한다.
'''