n = int(input())

for case in range(n):
    if case > 0:
        input()
        
    space = [list(map(int, input().split())) for _ in range(9)]
    rows = [set(space[i]) for i in range(9)]
    cols = [set(space[j][i] for j in range(9)) for i in range(9)]
    th_by_th = []
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            three = [space[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            th_by_th.append(set(three))
    
    def correct(sudoku):
        for line in sudoku:
            if len(line) < 9:
                return False
        return True
    
    if correct(rows) == correct(cols) == correct(th_by_th) == True:
        print(f'Case {case+1}: CORRECT')
    else:
        print(f'Case {case+1}: INCORRECT')
        