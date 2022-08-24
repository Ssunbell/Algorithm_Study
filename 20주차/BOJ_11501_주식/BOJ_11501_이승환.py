import sys

input_s = lambda : sys.stdin.readline().strip()

t = int(input_s())

for _ in range(t):
    n = int(input_s())
    price = list(map(int,input_s().split()))

    # 전체 계좌 수익
    acount = 0
    # 가장 높을때 판매하면 가장 큰 이득이기 때문에 가장 높은 주가를 저장
    max_price = 0

    # 마지막날부터 계산
    for i in range(n-1,0,-1):
        # 가장 높은 주가 저장
        max_price = max(max_price,price[i])
        # 전날 주식을 사서 지금까지의 가장 높은 금액에 파는것과 아무것도 안하는 것을 비교
        acount += max(0,max_price - price[i-1])

    print(acount)