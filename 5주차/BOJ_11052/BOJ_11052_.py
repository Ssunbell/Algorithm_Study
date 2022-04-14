n = int(input())
card = list(map(int, input().split()))
card = {i+1 : card[i] for i in range(n)}
print(card)
