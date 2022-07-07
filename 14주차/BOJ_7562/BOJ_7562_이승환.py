from collections import deque

t = int(input())

for _ in range(t):
    m = int(input())
    root_x, root_y = map(int,input().split())
    dest_x, dest_y = map(int,input().split())

    dx = [1,2,1,2,-1,-2,-1,-2]
    dy = [2,1,-2,-1,2,1,-2,-1]
    root = (root_x, root_y)
    dest = (dest_x, dest_y)

    q = deque()
    visited = deque()
    q.append(root)
    depth_chart = dict()
    depth_chart[root] = 0 
    
    if root == dest:
        result = 0

    while q:
        curr = q.popleft()
        visited.append(curr)
        
        if curr == dest:
            break

        for i in range(8):
            next = (curr[0]+dx[i],curr[1]+dy[i])
            if next[0] < 0 or next[1] < 0 or next[0] >= m or next[1] >= m:
                continue
            if next not in q and next not in visited:
                q.append(next)
                depth_chart[next] = depth_chart[curr] + 1
    
    result =  depth_chart[dest]

    print(result)