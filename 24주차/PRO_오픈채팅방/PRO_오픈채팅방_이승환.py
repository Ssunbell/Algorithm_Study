# result에는 아이디를 키로, 닉네임을 값으로 저장
# 첫번째 반복문에서는 answer에 메세지를 저장하면서 result에 닉네임을 갱신
# try문일경우에는 닉네임을 바꿀수 있는 "Enter"와 "Change"가 존재하므로 닉네임 갱신
# except문에서는 닉네임을 바꿀 수 없음.
# status가 "Enter"와 "Leave"일 경우만 메세지를 저장
# id&메세지 와 같은 형식으로 메세지를 저장, 두번째 반복문에서 split하여 아이디 참조
# 두번째 반복문에서는 answer에 저장된 아이디로 result에 닉네임을 참조하며
# answer에 닉네임을 붙여서 메세지 출력

def solution(record):
    answer = []
    result = dict()

    for r in record:
        try:
            status, id_, name = r.split()
            result[id_] = name
            if status == "Enter":
                answer.append(f"{id_}&님이 들어왔습니다.")
        except:
            status, id_ = r.split()
            answer.append(f"{id_}&님이 나갔습니다.")
    
    for i in range(len(answer)):
        id_, mes = answer[i].split("&")
        answer[i] = f"{result[id_]}" + mes
        
    return answer



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))