## 경우의 수 구하기
menu_idx = []
course_dict = {}
def dfs(input_string, course_length):
    if len(menu_idx) == course_length:
        menu = [input_string[idx] for idx in menu_idx]
        key = ''.join(sorted(menu))
        if key in course_dict:
            course_dict[key] += 1
        else:
            course_dict[key] = 1
        return
    
    
    for i in range(len(input_string)):
        if len(menu_idx) > 0 and menu_idx[-1] >= i:
            continue
        menu_idx.append(i)
        dfs(input_string, course_length)
        menu_idx.pop()
        

def solution(orders, course):
    ## 모든 경우의 수 추출
    for dish in orders:
        for cl in course:
            if len(dish) > cl:
                dfs(dish, cl)
            elif len(dish) == cl:
                dish = ''.join(sorted(dish))
                if dish in course_dict:
                    course_dict[dish] += 1
                else:
                    course_dict[dish] = 1

    ## 문자 길이가 인덱스가 되도록 2차원 리스트로 분류 
    courses_sorted = sorted(course_dict.items(), key=lambda x: (x[0], x[1]))
    courses_2D = [[] for _ in range(course[-1]+1)]
    for c in courses_sorted:
        dish, cnt = c[0], c[1]
        if cnt > 1:
            courses_2D[len(dish)].append(c)

    ## 2차원 리스트안에서 최대값인 문자열만 추출
    courses_1D = []
    for courses in courses_2D:
        if courses == []:
            continue
        else:
            courses_sorted = sorted(courses, key= lambda x: -x[1])

            max_v = courses_sorted[0][1]
            for course in courses_sorted:
                if course[1] == max_v:
                    courses_1D.append(course[0])
                else:
                    break
                    
    answer= sorted(courses_1D)
    
    return answer