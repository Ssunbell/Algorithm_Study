#[[3차]압축] -> 45점 받았습니다.
def solution(msg):
    #1.사전 초기화
    table = dict()
    for i, A in enumerate('ABCDEFGHIJKLMNOPQRSTUVXWYZ', start=1):
        table[A] = i

    answer = []
    index_num = 27
    i = 0
    w = msg[0]
    while i < len(msg):
        #2.사전에서 현재 입력과 일치하는 가장 긴 문자열 w찾기
        found = w
        while w in table:
            found = w
            i += 1
            if i == len(msg):
                break
            else:
                w += msg[i]
        #3.w에 해당하는 사전의 색인 번호 출력하고, 입력에서 w를 제거(30번째 줄)
        answer.append(table[found])
        #4.입력에서 처리되지 않은 다음 글자가 남아있다면, w+c에 해당하는 단어를 사전에 등록
        if len(w) > len(found):
            table[w] = index_num
            index_num += 1
        else:
            break
        w = w[-1]
    return answer