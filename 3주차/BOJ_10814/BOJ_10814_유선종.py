n = int(input())

customer = [tuple(input().split()) for _ in range(n)]
customer.sort(key=lambda x:int(x[0]))

for i in customer:
    print(i[0], i[1])