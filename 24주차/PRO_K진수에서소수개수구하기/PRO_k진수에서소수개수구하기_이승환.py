def convert_iter(num, base):
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

def solution(n, k):
    answer = -1
        
    
    return answer