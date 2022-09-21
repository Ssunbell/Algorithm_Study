from itertools import combinations
from collections import defaultdict

'''
ordered_dict
key : 주문내역에서 course 내 원소와 길이가 같은 모든 부분집합, String
value : key값에 대한 주문횟수

l_size_menus
ordered_dict에서 길이가 l이고 주문횟수가 2 이상인 모든 메뉴를 주문횟수 기준으로 내림차순 정렬한 것

list(zip(*filter(lambda x: x[1] == max_ordered_cnt, l_size_menus)))[0]
l_size_menus 에서 가장 많은 주문횟수를 가진 메뉴의 메뉴 이름을 저장하는 리스트
filter를 통해 주문횟수가 max_ordered_cnt와 같은 원소들을 l_size_menus에서 뽑아내어 zip하면 0번에는 메뉴명이, 1번에는 주문횟수가 저장됨. 메뉴명만 answer에 추가
'''


def solution(orders, course):
    ordered_dict = defaultdict(int)
    for order in orders:
        for l in course:
            for subset in combinations(order, l):
                ordered_dict[''.join(sorted(subset))] += 1
    answer = []
    for l in course:
        l_size_menus = sorted(filter(lambda x: len(
            x[0]) == l and x[1] != 1, ordered_dict.items()), key=lambda x: -x[1])
        if l_size_menus:
            max_ordered_cnt = l_size_menus[0][1]
            answer += list(zip(*filter(lambda x: x[1]
                           == max_ordered_cnt, l_size_menus)))[0]
    return sorted(answer)


tc = [[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
       ], [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
           ], [["XYZ", "XWY", "WXA"], [2, 3, 4]
               ]]
for c in tc:
    print(solution(*c))
