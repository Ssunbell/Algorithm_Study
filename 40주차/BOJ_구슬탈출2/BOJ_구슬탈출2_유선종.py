def qwer():
    for dx,dy in zip((-1,1,0,0),(0,0,-1,1)):
        yield dx, dy

def bfs():
    visited=[[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    q=[init_]
    visited[init_['ry']][init_['rx']][init_['by']][init_['bx']] = True
    while q:
        cur=q.pop(0)
        if cur['count'] > 10:
            return -1
        for dx, dy in qwer():
            rx, ry, bx, by = cur['rx'], cur['ry'], cur['bx'], cur['by']
            while array[bx + dx][by + dy] == ".":
                bx += dx
                by += dy

            if array[bx + dx][by + dy] == "O":
                continue

            while array[rx + dx][ry + dy] == ".":
                rx += dx
                ry += dy

            if array[rx + dx][ry + dy] == "O":
                return cur['count']
            
            if rx == bx and ry == by:
                if abs(rx-cur['rx']) + abs(ry-cur['ry']) > abs(bx-cur['bx']) + abs(by-cur['by']):
                    rx-=dx
                    ry-=dy
                else:
                    bx-=dx
                    by-=dy
            if not visited[ry][rx][by][bx]:
                visited[ry][rx][by][bx] = True
                next={}
                next['ry'],next['rx'],next['by'],next['bx']=ry,rx,by,bx
                next['count']=cur['count']+1
                q.append(next)
    return -1

N,M=map(int,input().split())
array=[list(input()) for _ in range(N)]
init_={'count' : 1}
for r in range(len(array)):
    for c in range(len(array[0])):
        if array[r][c] == 'R':
            init_['rx'], init_['ry']=r, c
            array[r][c] = '.'
        elif array[r][c] == 'B':
            init_['bx'], init_['by']=r, c
            array[r][c] = '.'
print(bfs())