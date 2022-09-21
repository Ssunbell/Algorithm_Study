def make_set(s):
    s = s.upper()
    s_list = []
    for i in range(1,len(s)):
        if s[i-1].isalpha() and s[i].isalpha():
            s_list.append(s[i-1]+s[i])
    return s_list
    
def solution(str1, str2):
    answer = 0
    
    list1 = make_set(str1)
    list2 = make_set(str2)

    # 교집합의 길이 -> a
    # 합집합의 길이 -> len(list_1+list2) - a
    # jab = a/(len(list_1+list2) - a)
    if list1 or list2:
        len_all = len(list1 + list2)
        its = 0
        # 교집합의 길이만 구하면 되기 때문에 숫자를 카운트해줌
        for s in list1:
            if s in list2:
                list2.remove(s)
                its += 1
        jab = its / (len_all - its)
    else:
        jab = 1

    answer = int(jab * 65536)
    return answer

print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))
