def convert_iter(num, base):
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

def solution(n, k):
    answer = -1
    # 소수를 어케찾을지 감이안오넹....
    
    return answer