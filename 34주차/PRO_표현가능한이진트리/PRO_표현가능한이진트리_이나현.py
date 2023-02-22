import math

def make_bytree(number):
    number = bin(number)[2:]
    length = len(number)
    h = math.ceil(math.log2(length+1))
    number = '0'*(2**h-1 - length) + number
    return number

def check_bytree(number):
    global result
    length = len(number)
    if length <= 1: #재귀 탈출조건
        return
    
    if number[length//2] == '1': #부모노드가 1이면 통과 -> 자식 tree 체크
        pass
    else:
        if number[length//4] == '0' and number[length*3//4] == '0': #부모노드가 0이고, 자식노드들도 0이면 통과
            pass
        else:                                                   #부모노드가 0이고, 자식노드들 중 하나라도 1이 있으면 불통과
            result = False
            return

    check_bytree(number[:length//2])   #왼쪽 트리
    check_bytree(number[length//2+1:]) #오른쪽 트리
    return

def solution(numbers):
    global result
    answer = []
    for number in numbers:
        result = True
        number = make_bytree(number)
        check_bytree(number)
        answer.append(1) if result == True else answer.append(0)
    return answer

print(solution([5]))
print(solution([7, 42, 5]))
