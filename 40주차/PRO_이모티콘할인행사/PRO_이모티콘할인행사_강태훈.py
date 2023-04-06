from itertools import product

def calc(user_rate, user_limit, item_prices, item_rates):
    total_price = 0
    for price, rate in zip(item_prices, item_rates):
        if rate >= user_rate:
            total_price += (100-rate)*price//100
            if total_price >= user_limit:
                return 1,0
    return 0,total_price

def solution(users, emoticons):
    answer = [0,0]
    for case in product((10,20,30,40), repeat=len(emoticons)):
        answer = max(answer, [sum(i) for i in zip(*[calc(*user, emoticons, case) for user in users])])
    return answer