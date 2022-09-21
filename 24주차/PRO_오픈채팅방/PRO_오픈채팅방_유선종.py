def solution(record):
    user_dict = {}
    for order, r in enumerate(record):
        command = r.split()[0]
        if command == 'Enter':
            _, userID, nickname = r.split()
            try:
                for idx,arr in enumerate(user_dict[userID]):
                    arr[1] = nickname
                user_dict[userID].append([order, nickname,'님이 들어왔습니다.'])
            except:
                user_dict[userID] = [[order, nickname,'님이 들어왔습니다.']]
        elif command == 'Leave':
            _, userID = r.split()
            user_dict[userID].append([order, user_dict[userID][-1][1],'님이 나갔습니다.'])
        elif command == 'Change':
            _, userID, nickname = r.split()
            for arr in user_dict[userID]:
                arr[1] = nickname

    answer = []
    for arr in user_dict.values():
        answer.extend(arr)
    answer = [arr[1] + arr[2] for arr in sorted(answer, key= lambda x: x[0])]
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))