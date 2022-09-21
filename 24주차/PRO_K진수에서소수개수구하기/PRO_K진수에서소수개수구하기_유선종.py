def convert_base_dec_to_n(num, base):
    value = []
    while num:
        q, r = divmod(num, base)
        value.append(str(r))
        num = q
    return ''.join(reversed(value))


def isprime(n):
    for i in range(2, 1 + int(n ** 0.5)):
        if n % i == 0:
            return False
    return False if n == 1 else True


def solution(n, k):
    return len(list(filter(lambda x: x and isprime(int(x)), convert_base_dec_to_n(n, k).split("0"))))


'''
convert_base_dec_to_n : 10진수를 n진수로 바꾼다.
isprime : 입력받은 수가 소수이면 True를, 아니면 False를 리턴한다.

10진수를 n진수로 변환하고 "0"으로 split한다. 0이 연속해서 등장하면 비어있는 문자열이 있을 수 있다.
filter를 이용하여 비어있지 않고 소수인 값만 포함하는 리스트를 만들고 그 길이를 리턴한다.
'''

tc = [[437674, 3], [110011, 10]]
for c in tc:
    print(solution(*c))
