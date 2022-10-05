import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
answer = 0

for i in range(n):
    seq = int(input())
    if seq > 1:
        positive.append(seq)
    elif seq == 1:
        answer += 1
    else:
        negative.append(seq)

positive.sort(reverse=True)
negative.sort()

if len(positive) % 2 == 0:
  for i in range(0, len(positive), 2):
    answer += positive[i] * positive[i+1]
else:
  for i in range(0, len(positive)-1, 2): 
    answer += positive[i] * positive[i+1]
  answer += positive[len(positive)-1] 

if len(negative) % 2 == 0: 
  for i in range(0, len(negative), 2):
    answer += negative[i] * negative[i+1]
else:
  for i in range(0, len(negative)-1, 2):
    answer += negative[i] * negative[i+1]
  answer += negative[len(negative)-1] 

print(answer)
