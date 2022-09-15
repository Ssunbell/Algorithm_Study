from collections import deque

N = int(input())
limit = sorted(deque((map(int,input().split())), reverse=True))
M = int(input())
box_weight = sorted(deque(map(int,input().split())), reverse=True)

if limit[0] < box_weight[0]:
    print(-1)
else:
    result, tmp, l = [], [], 0
    for i in range(len(box_weight)):
        while True:
            if box_weight[i] <= limit[l]:
                tmp.append(box_weight[i])
                
                if l == (len(limit)-1) or i == (len(box_weight)-1):
                    result.append(tmp)
                    tmp, l = [], 0
                    break
                
                l = (l + 1) % len(limit)

                break
            else:                
                if l == (len(limit)-1) or i == (len(box_weight)-1):
                    result.append(tmp)
                    tmp, l = [], 0
                    
                l = (l + 1) % len(limit)
    print(result)
    print(len(result))


'''
예)
[20, 20, 17, 11, 7, 7, 5, 5, 5, 2]
[18, 18, 17, 15, 15]
i = 0,
18(0) <= 20(0) --> 실어가라 [18]
i = 1,
18(1) <= 20(1) --> 실어가라 [18,18]
i = 2,
17(2) <= 17(2) --> 실어가라 [18,18,17]
i = 3,
15(3) > 11(3) --> 스톱 [18, 18, 17] 출바알!

i = 4,
15(4) <= 20(0) --> 실어가라 [15]
i = 5,
15(5) <= 20(1) --> 실어가라 [15,15]
[[18, 18, 17], [15, 15]] 의 len을 구하면 됨
'''