import sys
input = sys.stdin.readline

def transpose(graph:list) -> list:
    col = len(graph)
    row = len(graph[0])
    
    return [[graph[c][r] for c in range(col)] for r in range(row)]

def make_case(n:int, m:int):
    for i in range(2**(n*m)):
        yield bin(i)[2:].zfill(n*m)
        
def horizontal(case:list, n:int, m:int):
    yield from [list(map(int, case[row*m : row*m+m])) for row in range(n)]
    
def vertical(case:list, n:int, m:int):
    yield from transpose([list(map(int, case[row*m : row*m+m])) for row in range(n)])

def cut_graph(case:list, n:int, m:int):
    '''
    경우의 수 중에서 1일 경우 가로로 계산,
    0일 경우 세로로 계산
    가로로 계산할때는 raw_data,
    세로로 계산할때는 transpose
    '''
    global result
    hor = horizontal(case, n, m)
    ver = vertical(case, n, m)
    
    answer = 0
    tmp = ''
    for i, row in enumerate(hor):
        for j, check in enumerate(row):
            if check:
                tmp += paper[i][j]
            
            elif tmp and not check:
                answer += int(tmp)
                tmp=''
        
        if tmp:
            answer += int(tmp)
            tmp =''
    
    tmp = ''
    for i, row in enumerate(ver):
        for j, check in enumerate(row):
            if not check:
                tmp += paper_T[i][j]
                
            elif tmp and check:
                answer += int(tmp)
                tmp=''
                
        if tmp:
            answer += int(tmp)
            tmp = ''

    result = max(result, answer)
    
if __name__=='__main__':
    n, m = map(int, input().split())
    paper = [list(input().strip()) for _ in range(n)]
    paper_T = transpose(paper)
    result = 0
    for case in make_case(n, m):
        cut_graph(case, n, m)
        
    print(result)