from typing import List, Union
from copy import deepcopy

def reverse_row(array:List[List[int]], indices:List[int]) -> List[List[int]]:
    for idx in indices:
        array[idx] = [element ^ 1 for element in array[idx]]
    
    return array

def check_col(array:List[List[int]], target:List[List[int]])-> Union[int, bool]:
    cnt = 0
    for col_idx in range(len(target[0])):
        target_col = []
        array_col = []
        array_col_r = []
        for row_idx in range(len(target)):
            target_col.append(target[row_idx][col_idx])
            array_col.append(array[row_idx][col_idx])
            array_col_r.append(array[row_idx][col_idx] ^ 1)
        if array_col_r == target_col:
            cnt += 1
        elif array_col == target_col:
            pass
        else:
            return False
        
    return cnt

def solution(beginning, target):
    '''
    행과 열을 무한히 뒤집는 것이 아닌
    각 행과 열을 한번씩만 뒤집는 문제
    즉, 2행을 한번 뒤집었다면 다시 2행을 뒤집을 수 없음
    '''
    row_cases = []
    tmp = []
    def dfs(depth):
        if len(tmp) == depth:
            row_cases.append(tuple(tmp))
            return
        
        for number in range(len(target)):
            if len(tmp) > 0 and tmp[-1] >= number:
                continue
            tmp.append(number)
            dfs(depth)
            tmp.pop()
    
    for i in range(len(target)+1):
        dfs(i)

    cnt = float('inf')
    for case in row_cases:
        array = deepcopy(beginning)
        array = reverse_row(array, list(case))
            
        count_or_false = check_col(array, target)
        if count_or_false != False:
            cnt = min((len(case) + count_or_false), cnt)

    return -1 if cnt == float('inf') else cnt