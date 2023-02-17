from typing import *

def check_perfect(i:int, number:int) -> Union[int, Callable]:
    if 2**(i-1) < number <= 2**i:
        return 2**i - 1
    else:
        return check_perfect(i+1, number)
    
def dfs(bin_num:List[int], p:int, depth:int) -> int:
    if depth == 0:
        return 1
    elif bin_num[p] == '0':
        if bin_num[p-depth] == '1' or bin_num[p+depth] == '1':
            return 0
        
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
            
        if '1' in bin(p_len)[3:]: # 만약 2의 n 제곱승이 아니라면 (ex: 111)
            bin_num = '0'*(p_len-len(bin_num)) + bin_num
        is_p_bin = dfs(bin_num, len(bin_num)//2, (p_len+1)//4)
        answer.append(is_p_bin)

    return answer