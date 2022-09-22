#[k진수에서 소수 개수 구하기]
from collections import deque

def convert_base(n, k):
    result = deque()
    while n:
        result.appendleft(n % k)
        n //= k
    result = "".join(map(str, result))
    return result


def isprime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True


def solution(n, k):
    arr = list(convert_base(n,k).split('0'))
    answer = 0
    for num in arr:
        if num and isprime(int(num)):
            answer += 1
    return answer

test = [[100, 10],
        [17001700170170, 10],
        [11011, 10],
        [17, 10],
        [1, 10],
        [102, 10],
        [437674, 3],
        [110011, 10]]
for n, k in test:
    print(solution(n,k))