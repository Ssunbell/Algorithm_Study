from typing import List

def solution(
    enroll:List[str],
    referral:List[str],
    seller:List[str],
    amount:List[int]
    )-> List[int]:
    
    answer = [0 for _ in range(len(enroll))]
    enroll_dict = {e:i for i, e in enumerate(enroll)}
    
    for s, a in zip(seller, amount):
        money = a * 100
        while s != "-" and money > 0:
            idx = enroll_dict[s]
            answer[idx] += money - money//10
            money //= 10
            s = referral[idx]
            
    return answer