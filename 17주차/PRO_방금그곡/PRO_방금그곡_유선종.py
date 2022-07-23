
def solution(m, musicinfos):
    melody_dict = {'a':'C#', 'b':'F#', 'c':'D#', 'd':'G#', 'e':'A#', 'f':'F',
                       'g':'C', 'h':'G', 'i':'D', 'j':'A', 'k':'E', 'l':'B'}
    
    for node, re in melody_dict.items():
        m = m.replace(re, node)
    
    melody_list = []
    for row in musicinfos:
        # 재생시간 구하기
        row = row.split(',')
        tmp_time = row[0].split(':')
        h1, m1 = int(tmp_time[0]), int(tmp_time[1])
        tmp_time = row[1].split(':')
        h2, m2 = int(tmp_time[0]), int(tmp_time[1])
        cycle = ((h2 - h1) * 60 + m2 - m1)
        
        # 악보에 사용되는 음 치환
        melody = row[-1]
        for node, re in melody_dict.items():
            melody = melody.replace(re, node)
            
        tmp_mel = ''
        for i in range(cycle):
            tmp_mel += melody[i % len(melody)]
        melody_list.append([cycle, tmp_mel])
    
    answer = []
    for i, mel in enumerate(melody_list):
        if m in mel[1]:
            answer.append([mel[0],musicinfos[i].split(',')[2]])

    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][1]
    else:
        answer = sorted(answer, key=lambda x: -x[0])
        return answer[0][1]

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))