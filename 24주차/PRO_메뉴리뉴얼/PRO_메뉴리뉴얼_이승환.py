from itertools import combinations

# 각 주문별로 나올 수 있는 모든 조합을 도출하고,
# 딕셔너리에 등장횟수를 저장함
def solution(orders, course):
    answer = []
    # 코스 길이가 각각 달라서 어떻게할지 최대값을 어떻게 할까 고민하다가
    # 코스길이별로 딕셔너리에 저장하고 뽑아내는 방식을 선택
    for i in course:
        all_menu = []
        # 코스길이 i로 나올수 있는 모든 음식조합을 가져옴
        # xy, yx는 같은걸로 간주하기 떄문에 모든 메뉴는 정렬을 한 뒤 조합을 뽑음
        for order in orders:
            sorted_order = sorted(order)
            a = list(combinations(sorted_order,i))
            all_menu += a
        
        # 딕셔너리에 하나씩 저장, 재등장시 +1
        course_dict = dict()
        for menu in all_menu:
            if menu in course_dict:
                course_dict[menu] += 1
            else:
                course_dict[menu] = 1
        
        # 딕셔너리에 값이 존재하면 max값을 저장, 아닐시 넘어감
        if course_dict:
            max_val = max(course_dict.values())
        else:
            continue
        
        # 딕셔너리를 순회하면서 값이 2이상이거나 max값보다 크다면 코스에 저장
        # 코스에 저장할떄는 튜플형태로 저장되어있는 menu를 str로 합쳐줌
        for menu, num in course_dict.items():
            if num >= max_val and num >= 2:
                course_name = ""
                for s in menu:
                    course_name += s
                answer.append(course_name)
    
    answer = sorted(answer)

    return answer


k = [[["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4],["AC", "ACDE", "BCFG", "CDE"]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5],["ACD", "AD", "ADE", "CD", "XYZ"]],
    [["XYZ", "XWY", "WXA"],[2,3,4],["WX", "XY"]]]

i = 0
for orders,course,answer in k:
    i+=1
    my_answer = solution(orders,course)
    if my_answer == answer:
        print(my_answer, f"케이스{i} 정답")
    else:
        print(f"케이스{i} 오답")
        print(my_answer,answer)