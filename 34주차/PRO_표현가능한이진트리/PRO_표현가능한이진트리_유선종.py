from typing import *

def check_perfect(i:int, number:int) -> Union[int, Callable]:
    if 2**(i-1) < number <= 2**i:
        # 2의 n승 포화 이진트리의 n 구하기
        return 2**i - 1
    else:
        return check_perfect(i+1, number)
    
def dfs(bin_num:List[int], p:int, depth:int) -> int:
    if depth == 0:
        return True
    elif bin_num[p] == '0':
        if bin_num[p-depth] == '1' or bin_num[p+depth] == '1':
            # 부모 노드가 0인데 자식 노드가 1인 경우는 표현할 수 없는 포화 이진트리
            return False
        
    left = dfs(bin_num, p - depth, depth//2) # 왼쪽 탐색
    right = dfs(bin_num, p + depth, depth//2) # 오른쪽 탐색
    
    return 1 if left and right else 0

def solution(numbers:List[int]) -> List[int]:
    answer = []
    for number in numbers:
        bin_num = bin(number)[2:] # 이진수로 바꿔줌 (ex: 42 -> 101010)
        if len(bin_num) > 1:
            p_len = check_perfect(1, len(bin_num))
        else:
            p_len = 1
            
        bin_num = '0'*(p_len-len(bin_num)) + bin_num
        is_p_bin = dfs(bin_num, len(bin_num)//2, (p_len+1)//4)
        answer.append(is_p_bin)

    return answer