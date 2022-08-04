import itertools
import math

def solution(numbers):
    nums = list(map(str,numbers))
    permutationlist= []
    answer_list = []
    for i in range(len(nums)):
        for j in itertools.permutations(nums, i+1):
                permutationlist.append(int(''.join(j)))

    permutationlist = list(set(permutationlist))

    for n in set(permutationlist):
        count = 0
        for m in range(2, int(math.sqrt(n))+1):
            if n % m == 0:
                count += 1
            if n > 1 and count == 0:
                answer_list.append(n)
    answer = len(set(answer_list))
    return answer
    

print(solution("011"))