from bisect import bisect_left
classification_dict = {
    "-": 0, "python": 1, "cpp": 2, "java": 3,
    "backend": 1, "frontend": 2,
    "senior": 1, "junior": 2,
    "pizza": 1, "chicken": 2
}


def solution(info, query):
    users = [[[[[] for _ in range(3)] for _ in range(3)]
              for _ in range(3)] for _ in range(4)]
    for i in info:
        a, b, c, d, score = i.split()
        a, b, c, d = list(map(lambda x: classification_dict[x], [a, b, c, d]))
        for q in (a, 0):
            for w in (b, 0):
                for e in (c, 0):
                    for r in (d, 0):
                        users[q][w][e][r].append(int(score))
    for a in range(4):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    users[a][b][c][d].sort()
    answer = []
    for q in query:
        a, b, c, d = q.split(" and ")
        d, score = d.split()
        score = int(score)
        a, b, c, d = list(map(lambda x: classification_dict[x], [a, b, c, d]))
        answer.append(len(users[a][b][c][d]) -
                      bisect_left(users[a][b][c][d], score))
    return answer


'''
4 * 3 * 3 * 3 리스트 users를 생성한다. 각각 언어, 포지션, 경력, 음식을 의미한다.
classification_dict에 요소 별 인덱스를 기입한다. 단, "-"이 0이다.
info 내 모든 정보에 대해 score를 제외한 모든 정보를 "-" 로 바꿀경우, 바꾸지 않을 경우를 고려하여 모두 users에 저장한다. 

예를들어 java backend junior pizza 150의 경우
java backend junior pizza
java backend junior -
java backend - pizza
~
java - - -
- - - -
로, 16개의 위치에 score를 append한다.
info에 대해 기록을 완료하면 리스트를 모두 정렬한다.

이후 query 조건에 맞는 리스트에 접근한다.
이분탐색 라이브러리 bisect를 사용하여 score 이상인 값이 처음 나오는 위치의 인덱스를 구한다.
([1,2,3,4,5], score = 3이라면 bisect_left(arr, score)은 2이다.)
이를 리스트 총 길이에 빼서 answer에 append한다.


'''

tc = [[["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
    "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]]]
for c in tc:
    print(solution(*c))
