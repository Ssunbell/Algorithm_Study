#[프로그래머스_2차원뒤집기]
# 모든 행에 대해 뒤집을 수 있는 경우를 고려(브루트포스)
# 행을 뒤집을 땐 비트마스킹으로 뒤집을 행을 확인하며 뒤집는다.
# 행을 뒤집은 후 열에 대해서도 뒤집어야할 때 뒤집기
# 행/열 뒤집기가 끝난 후(compare) target과 비교
# 같다 -> cnt 리턴, 가능한 경우가 없다 -> -1 리턴
# 4케이스 통과 못했습니다.


from copy import deepcopy
def solution(beginning, target):
    
    def row_flip(row):
        compare[row] = [toggle[x] for x in compare[row]]
    
    def col_flip(col, height):
        for i in range(height):
            compare[i][col] = toggle[compare[i][col]]

    def check(height, width):
        for i in range(height):
            for j in range(width):
                if compare[i][j] != target[i][j]:
                    return False
        return True

    height = len(beginning)
    width = len(beginning[0])
    toggle = {1:0, 0:1}
    for case in range(2**(height)): #모든 행뒤집기 경우의 수
        cnt = 0
        compare = deepcopy(beginning)
        for index in range(height): #index를 돌며 뒤집어야하는 확인 후 행 뒤집기
            if case & (1 << index):
                cnt += 1
                row_flip(index)
        for j in range(width):     #row 다 뒤집은 후 col 뒤집기
            if compare[0][j] != target[0][j]: #해당 열의 첫번쨰 행값이 다르면 뒤집는다.
                cnt += 1
                col_flip(j, height)
        if check(height, width): #해당 케이스가 잘 뒤집었다면 cnt를 리턴
            return cnt
    
    return -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))