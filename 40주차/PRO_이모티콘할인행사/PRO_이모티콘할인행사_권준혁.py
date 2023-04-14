from itertools import product

def solution(users, emoticons):
    result = []
    for p in product([0.1, 0.2, 0.3, 0.4], repeat=len(emoticons)):
        plus, sold = 0, 0
        for u in users:
            ratio, price = u
            total = 0
            for e, r in zip(emoticons, p):
                if r >= ratio * 0.01:
                    total += e * (1 - r)
            if total >= price:
                plus += 1
            else:
                sold += total
        result.append([plus, int(sold)])
    result.sort(key=lambda x:(-x[0], -x[1]))
    return result[0]