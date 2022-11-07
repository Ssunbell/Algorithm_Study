def solution(gems):
    # # 이 풀이는 효율성 통과를 못하고 반례가 발생한다.
    # # ["A", "AA", "AA", "AAA", "AA", "A"]
    # # 실행한 결괏값 [1,4]이 기댓값 [4,6]과 다릅니다.
    # # 전체 범위에서 좁혀나가는 방식을 생각했는데,
    # 이렇게 될 경우 좌, 우 중 어떤 포인터를 이동시킬지 결정 지을 때 반례가 발생한다.
    # 물론 좌측과 우측 각각의 경우에 대해 모두 구해서 st가 제일 작은 경우를 택하면 되긴 하지만,
    # 연산을 2번해서 비효율적이므로 투 포인터 모두 좌측에서 시작되는 경우로 풀이한다.
    # st = 0
    # en = len(gems) - 1
    # while(0 <= st < en):
    #     if (gems[en] in set(gems[st + 1:en])) or (gems[en] == gems[st]):
    #         en -= 1
    #     elif (gems[st] in set(gems[st + 1:en])):
    #         st += 1
    #     else:
    #         break
    # return [st + 1,en + 1]
    
    # 좌측에서부터 출발하는 투포인터 풀이
    st = 0
    en = 0
    len_g = len(set(gems))
    dic = {gems[0]:1}
    answer = [1, len(gems)]
    if len_g == 1:
        return [1,1]
    while(st < len(gems) and en < len(gems)):
        if len(dic) == len_g:
            if answer[1] - answer[0] > en - st:    
                answer[0] = (st + 1)
                answer[1] = (en + 1)
            dic[gems[st]] -= 1
            if dic[gems[st]] == 0:
                del dic[gems[st]]
            st += 1
        else:
            en += 1
            if en == len(gems):
                return answer
            dic[gems[en]] = dic.get(gems[en], 0) + 1
    return answer

print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution([1,2,3,4,1,2,3,4]))