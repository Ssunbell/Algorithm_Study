import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
sequence = sorted([int(input()) for _ in range(n)], reverse=True)
if n == 1:
    print(sequence[0])
else:
    positive = []
    negative = []
    one_list = []
    answer = 0
    for num in sequence:
        if num > 1:
            positive.append(num)
        elif num <= 0:
            negative.append(num)
        else:
            one_list.append(1)

    positive.sort(reverse=True)
    negative.sort()
    
    if len(positive) % 2 == 0:
        for i in range(0, len(positive), 2):
            answer += positive[i] * positive[i+1]
    else:
        for i in range(0, len(positive)-1, 2):
            answer += positive[i] * positive[i+1]
        answer += positive[-1]
    if len(negative) % 2 == 0:
        for i in range(0, len(negative), 2):
            answer += negative[i] * negative[i+1]
    else:
        for i in range(0, len(negative)-1, 2):
            answer += negative[i] * negative[i+1]
        answer += negative[-1]
    
    answer += len(one_list)
    print(answer)
    
# jump = False
# if n == 1:
#     print(sequence[0])
# else:
#     if n % 2 == 0:
#         for i in range(0, len(sequence)-1):
#             if jump == True:
#                 jump = False
#                 continue
#             if sequence[i] > 1 and sequence[i+1] > 1:
#                 result.append((sequence[i], sequence[i+1]))
#                 jump = True
#             elif sequence[i] > 1 and 0 <= sequence[i+1] < 2:
#                 result.append(sequence[i])
#                 result.append(sequence[i+1])
#                 jump = True
#             elif 0 <= sequence[i] < 2 and 0 <= sequence[i+1] < 2:
#                 result.append(sequence[i])
#                 result.append(sequence[i+1])
#                 jump = True
#             elif sequence[i] == 1 and sequence[i+1] < 0:
#                 result.append(sequence[i])
#                 result.append(sequence[i+1])
#                 jump = True
#             elif sequence[i] == 0 and sequence[i+1] < 0:
#                 result.append((sequence[i], sequence[i+1]))
#                 jump = True
#             elif sequence[i] < 0 and sequence[i+1] < 0:
#                 result.append((sequence[i], sequence[i+1]))
#                 jump = True
#     else:
#         result.append(sequence[0])
#         for i in range(1, len(sequence)):
#             if jump == True:
#                 jump = False
#                 continue
#             if sequence[i] > 1 and sequence[i+1] > 1:
#                 result.append((sequence[i], sequence[i+1]))
#                 jump = True
#             elif sequence[i] > 1 and 0 <= sequence[i+1] < 2:
#                 result.append(sequence[i])
#                 result.append(sequence[i+1])
#                 jump = True
#             elif 0 <= sequence[i] < 2 and 0 <= sequence[i+1] < 2:
#                 result.append(sequence[i])
#                 result.append(sequence[i+1])
#                 jump = True
#             elif sequence[i] == 1 and sequence[i+1] < 0:
#                 result.append(sequence[i])
#                 result.append(sequence[i+1])
#                 jump = True
#             elif sequence[i] == 0 and sequence[i+1] < 0:
#                 result.append((sequence[i], sequence[i+1]))
#                 jump = True
#             elif sequence[i] < 0 and sequence[i+1] < 0:
#                 result.append((sequence[i], sequence[i+1]))
#                 jump = True