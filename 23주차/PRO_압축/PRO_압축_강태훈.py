def solution(msg):
    # 길이 1인 모든 단어를 포함하도록 사전 초기화
    zip_dict = {chr(ord("A") + i): i + 1 for i in range(26)}
    answer = []

    def zip_text(txt):
        # 종료조건, txt가 사전에 존재할 경우 txt의 색인번호를 출력하고 종료
        if txt in zip_dict.keys():
            return answer + [zip_dict[txt]]
          
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기 (w = txt[s:e - 1])
        s, e = 0, 1
        while txt[s:e] in zip_dict.keys() and e < len(txt):
            e += 1
            
        # w에 해당하는 사전의 색인번호를 출력, 사전에 w + c 등록
        # 재귀호출하여 남은 문자열에 대해서도 위 과정 반복
        zip_dict[txt[s: e]] = len(zip_dict) + 1
        answer.append(zip_dict[txt[s: e - 1]])
        return zip_text(txt[e - 1:])
      
    return zip_text(msg)


test_case = ["KAKAO",
             "TOBEORNOTTOBEORTOBEORNOT",
             "ABABABABABABABAB"]
for text in test_case:
    print(solution(text))

'''
입력 msg의 최대 길이가 1000글자로 짧은 편이다. 극단적으로 한글자씩만 처리한다고 하더라도 파이썬 기본 재귀함수 깊이인 1000 내에서 처리할 수 있다.
사전에 존재하는 가장 긴 문자열을 찾고 출력한 후 한글자 붙혀 사전에 추가하고 색인번호를 부여하는 과정을 반복한다.
재귀함수의 종료조건은 입력 문자열이 이미 사전에 존재할 경우로 설정했다.
'''
