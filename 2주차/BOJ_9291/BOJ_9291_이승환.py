testcase_num = int(input())

def check_sudoku(a):
    for i in range(9):
        sudoku = set(a[i])
        if len(sudoku) < 9 :
            return False
    return True

for t in range(testcase_num):
    if t > 0:
        input()

    sudoku = [list(map(int, input().split())) for i in range(9)]
    sudoku_row = [i for i in sudoku]
    sudoku_col = [list(sudoku[i][j] for i in range(9)) for j in range(9)]
    sudoku_square = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s_s = sudoku[i][j:j+3] + sudoku[i+1][j:j+3] + sudoku[i+2][j:j+3]
            sudoku_square.append(s_s)
    
    row_check = check_sudoku(sudoku_row)
    col_check = check_sudoku(sudoku_col)
    square_check = check_sudoku(sudoku_square)

    if row_check and square_check and col_check:
        print(f"Case {t+1}: CORRECT")
    else:
        print(f"Case {t+1}: INCORRECT")


""" import pandas as pd

testcase_num = int(input())

for t in range(testcase_num):
    if t>1:
        input()
    sudoku = []
    for i in range(9):
        s_row = list(map(int, input().split()))
        sudoku.append(s_row)
    df_sudoku = pd.DataFrame(sudoku)

    true_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    true_list = pd.Series(true_list)

    row_check = False
    for i in range(9):
        list_sudoku_row = df_sudoku.iloc[i].tolist()
        row_info = true_list.isin(list_sudoku_row)
        if row_info.all():
            row_check = True
        else:
            row_check = False
            break

    col_check = False
    for i in range(9):
        list_sudoku_col = df_sudoku[i].tolist()
        col_info = true_list.isin(list_sudoku_col)
        if col_info.all():
            col_check = True
        else:
            col_check = False
            break

    square_check = False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            df_square = df_sudoku.iloc[i:i+3, j:j+3]
            list_sudoku_square = sum(df_square.values.tolist(), [])
            square_info = true_list.isin(list_sudoku_square)
            if square_info.all().all():
                square_check = True
            else:
                square_check = False

    if row_check and col_check and square_check:
        print(f"Case {t+1}: CORRECT")
    else:
        print(f"Case {t+1}: INCORRECT")
 """
