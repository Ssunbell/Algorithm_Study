from math import log2

def check(full_b, parent):
    if parent == '0':
        for child in full_b:
            if child == '1':
                return False
    if len(full_b) == 1:
        return True
    left = full_b[:len(full_b) // 2]
    right = full_b[len(full_b) // 2 + 1:]
    return check(left, left[len(left) // 2]) and check(right, right[len(right) // 2])

def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]
        depth = int(log2(len(b))) + 1
        len_node = 2 ** depth - 1
        full_b = '0' * (len_node - len(b)) + b
        if check(full_b, full_b[len(full_b) // 2]):
            answer.append(1)
        else:
            answer.append(0)
    return answer