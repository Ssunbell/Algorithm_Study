#[뉴스 클러스터링]
from collections import Counter

def create_arr(str):
    arr = []
    for i in range(len(str)-1):
        tmp = str[i:i+2]
        if 'a' <= tmp[0] <= 'z' and 'a' <= tmp[1] <= 'z':
            arr.append(tmp)
    return arr

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_arr = create_arr(str1)
    str2_arr = create_arr(str2)
    str1_cnt = Counter(str1_arr)
    str2_cnt = Counter(str2_arr)
    intersection = str1_cnt & str2_cnt
    union = str1_cnt | str2_cnt
    if sum(union.values()) == 0: 
        return 65536
    answer = int(sum(intersection.values()) / sum(union.values()) * 65536)
    return answer

test = [['FRANCE', 'french'], \
        ['handshake', 'shake hands'], \
        ['aa1+aa2', 'AAAA12'], \
        ['E=M*C^2', 'e=m*c^2']]
for str1, str2 in test:
    print(solution(str1,str2))