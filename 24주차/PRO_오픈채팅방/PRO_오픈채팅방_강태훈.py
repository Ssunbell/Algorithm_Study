def solution(record):
    print_format = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    record = list(map(lambda x: x.split(), record))

    nicknames = {data[1]: data[2] for data in filter(lambda x: x[0] != "Leave", record)}

    answer = [nicknames[data[1]] + print_format[data[0]] for data in filter(lambda x: x[0] != "Change", record)]
    return answer


'''
nicknames : id를 key로 최종 nickname을 받아옴
answer : Change를 제외한 record의 형식을 바꾸어 저장함
'''


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
