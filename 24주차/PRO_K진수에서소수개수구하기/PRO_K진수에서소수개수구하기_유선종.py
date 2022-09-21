def solution(n, k):
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k
    prime = tmp[::-1]
    answer = prime.split('0')
    count = 0
    for num in answer:
        if num == '1' or num == '':
            continue
        num = int(num)
        count += 1
        for i in range(2,int(int(num)**0.5)+1):
            if int(num)%i==0:
                count -= 1
                break
    return count

tc = [[437674, 3], [110011, 10]]
for c in tc:
    print(solution(*c))
