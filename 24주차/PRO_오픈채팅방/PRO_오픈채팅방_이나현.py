#[오픈 채팅방]
from collections import defaultdict
def solution(record):
    user_table = defaultdict()
    action_table = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    action_id = []
    for r in record:
        r = list(r.split())
        nick = ""
        if len(r) == 3:
            action, id, nick = r
        else:
            action, id = r
        if nick:
            user_table[id] = nick
        if action != 'Change':
            action_id.append([id, action]) #"['uid1234', 'Enter']
    answer = []
    for a in action_id:
        s = ''
        s += user_table[a[0]]
        s += action_table[a[1]]
        answer.append(s)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))