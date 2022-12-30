#[프로그래머스_다단계칫솔판매]
from collections import defaultdict
# 구현
# 모든 거래(seller, amount)를 for문으로 돌면서, 정산을 합니다.
# 실제로 판 seller는 0.9의 수익을 갖게되고,
# 그 seller의 부모는 0.1의 수익을 받았다가, 그 금액에서 0.1을 그 부모(seller의 부모의 부모)에게 줍니다.

def solution(enroll, referral, seller, amount):

    def sharing_profit(profit, who):
        while profit * 0.1 >= 1:
            who = parent_dict[who]
            if who == '-':
                break
            real_profit[who] += int(profit * 0.1) #자식의 이익 10%를 받았다가
            profit = profit * 0.1
            real_profit[who] -= int(profit * 0.1) #자신의 부모에게 그 받은 것의 10%를 주는 부분
            
    real_profit = defaultdict(lambda:0) #최종 이익
    parent_dict = {}
    for i in range(len(enroll)): #누가 부모인지?
        parent_dict[enroll[i]] = referral[i]

    for who, how_many in zip(seller, amount): #발생한 모든 거래
        profit = how_many * 100
        real_profit[who] += int(profit * 0.9)
        sharing_profit(profit, who)

    answer = []
    for who in enroll:
        answer.append(real_profit[who])
    return answer


# 순영업이익을 한번에 합산한 뒤 정산하면 안된다.
# 왜냐, 동일인물이 100원, 900원 이익을 냈다면 100->1->0, 900->9->0 이기 때문에
# 합산했을 때와 1000->100->10->1 결과가 달라진다.


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))