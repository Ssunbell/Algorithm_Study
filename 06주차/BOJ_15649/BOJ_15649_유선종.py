n, m = map(int, input().split())

storage = []
visited = [False] * (n+1)

def backtracking():
    if len(storage) == m:
        print(' '.join(map(str, storage)))
        return
    
    for stair in range(1, n+1):
        if visited[stair] == True:
            continue
        visited[stair] = True
        storage.append(stair)
        backtracking()
        storage.pop()
        visited[stair] = False
        
backtracking()

'''
예시) 만약, (1,2,3)을 출력하고자 한다면 처음에 1에서 시작한다.
1이 처음이므로 visited[1]은 False이고, 출력값을 저장할 storage 또한 아무것도 없다.
이때, 방문했다는 표시를 위해 visited[1] = True로 바꿔준다.
바꿔준 후, storage에 해당 숫자를 넣어준다.
이때, 우리는 (1,2,3)의 3개의 숫자를 출력해야 하므로, len(storage) == 3이 될때까지 반복한다.
이 반복은 backtracking 함수 안에 backtracking을 넣어(dfs) 반복실행하도록 만든다.
만약, len(storage) == 3을 만족하면 해당 storage를 출력하고 storage.pop으로 (1,2)로 돌아오고 visited[3]을 False로 바꿔준다.
다시 for문에 의해서 backtracking이 실행되면서 반복된다.
1에서 n까지 모두 돌게 되면 더이상 사용할 숫자가 없으므로 빠져나오게 된다. (3중 for문)
'''