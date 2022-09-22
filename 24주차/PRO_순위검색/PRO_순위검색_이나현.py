# 정확성은 다 맞았으나, 효율성은 0점 받은 코드입니다.
index_table = {'cpp':0, 'java':1, 'python':2, \
               'backend':0, 'frontend':1, \
               'junior':0, 'senior':1, \
               'chicken':0, 'pizza':1, \
               '-':-1}

cnt = 0
where = []
condition = []
def search(level, tmp, pos): #level= 언어 : 0, 직무 : 1, 경력 : 2, ...
    global cnt, where, condition
    if level == 3:
        if pos == -1:
            tmp = tmp[0] + tmp[1]
        else:
            tmp = tmp[pos]
        for score in tmp:
            if int(score) >= int(condition[4]):
                cnt += 1
        return
    tmp2 = tmp[:]
    if pos == -1 and level == 0:
        for i in range(3):
            tmp = tmp2
            tmp = tmp[i]
            search(level+1, tmp, where[level+1])
    elif pos == -1:
        for i in range(2):
            tmp = tmp2
            tmp = tmp[i]
            search(level+1, tmp, where[level+1])
    else:
        tmp = tmp[where[level]]
        search(level+1, tmp, where[level+1])

def solution(info, query):
    global cnt, where, condition
    #5차원 리스트 : 언어 - 직군 - 경력 - 소울푸드 - 점수
    applicants = [[[[[],[]],[[],[]]],[[[],[]],[[],[]]]],[[[[],[]],[[],[]]],[[[],[]],[[],[]]]],[[[[],[]],[[],[]]],[[[],[]],[[],[]]]]]
    #지원자 분류하기
    for person in info:
        person = list(person.split())
        where = [0] * 4
        for i in range(4):
            where[i] = index_table[person[i]]
        applicants[where[0]][where[1]][where[2]][where[3]].append(person[4])
    answer = []
    #조건 인덱스화 시키기(where 배열)
    for condition in query:
        condition = list(condition.split(' and '))
        condition = condition[:3] + list(condition[3].split())
        where = [0] * 4
        for i in range(4):
            where[i] = index_table[condition[i]]
        cnt = 0
    #조건에 맞는 사람 수 계산
        search(0, applicants, where[0])
        answer.append(cnt)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]
print(solution(info, query))