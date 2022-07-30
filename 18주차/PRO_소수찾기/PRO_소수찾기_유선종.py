primeSet = set()

def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, int(int(number) ** (1/2)) + 1):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))
    print('우리는 ', str1, '의 세상에 살고있다')

    for i in range(len(str2)):
        print('str1 ',str1 + str2[i])
        print('str2 ',str2[:i], 'second:', str2[i + 1:])
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer

n = "101"
solution(n)
