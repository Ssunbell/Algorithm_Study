def make_iter(emoji_len):
    for i in range(2**(2*emoji_len)):
        bin_str = format(i, 'b').zfill(2*emoji_len)
        yield list(map(lambda x:10*(1+int(x,2)), (bin_str[j:j+2] for j in range(0, 2*emoji_len, 2))))
        
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
    for case in make_iter(len(emoticons)):
        answer = max(answer, [sum(i) for i in zip(*[calc(*user, emoticons, case) for user in users])])
    return answer