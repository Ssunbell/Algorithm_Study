n = int(input())
house_list = sorted(list(map(int, input().split())))
if len(house_list) % 2 == 0:
    print(house_list[(len(house_list) // 2) - 1])
else:
    print(house_list[len(house_list) // 2])
'''
1,2,3,4,9,20일때,
2 - (2-1) + (20-2) = 1 + 18 = 19
3 - (3 -1) + (20-3) = 2 + 17 = 19
4 - (4-1) + (20 - 4) = 3 + 16 = 19
9 - (9-1) + (20 - 9) = 8 + 11 = 19

양 끝 값들(1,20)을 내부 값을 기준으로 거리를 측정하면 모두 동일하게 나옴
따라서 가장 가운데에 위치하게 되면 됨
근데 여기서 set()을 하면 틀림;; 왜 그런지는 모르겠음
'''


