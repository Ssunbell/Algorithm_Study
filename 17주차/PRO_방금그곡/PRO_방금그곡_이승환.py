def get_play_time(start,finish):
    start_hours = int(start[:2]) * 60
    start_min = int(start[3:5])
    start_time = start_hours + start_min
    
    # if finish == "00:00":
    #     finish = "24:00"
    finish_hours = int(finish[:2]) * 60
    finish_min = int(finish[3:5])
    finish_time = finish_hours + finish_min

    playtime = finish_time - start_time
    
    return playtime

def solution(m, musicinfos):
    answer = ''
    playlist = []
    playlist_time = []
    for infos in musicinfos:
        start,finish,title,music = infos.split(",")
        
        # 총 재생시간 구하기
        play_time = get_play_time(start,finish)
        
        # 악보를 리스트로 변형하고, #음은 소문자로 변경
        musics = []
        for ms in music:
            if ms != "#":
                musics.append(ms)
            else:
                musics[-1] = musics[-1].lower()
        mm = []
        for i in m:
            if i != "#":
                mm.append(i)
            else:
                mm[-1] = mm[-1].lower()
        m = ""
        for i in mm:
            m += i
        
        # 재생된 멜로디 저장
        melody = ""
        for time in range(play_time):
            note = time % len(musics)
            melody += musics[note]
        
        # 재생된 멜로디가 조건에 일치할 경우 해당 음악 정보 저장
        if m in melody:
            playlist.append(title)
            playlist_time.append(play_time)
    
    # 재생시간이 제일 길고 가장 먼저 입력된 음악 반환
    if playlist:
        for i in range(len(playlist)):
            if playlist_time[i] == max(playlist_time):
                answer = playlist[i]
                break   
    else:
        answer = "(None)"
    return answer


# m = "ABCDEFG"
# mi = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m = "CC#BCC#BCC#"
mi = ["03:00,03:08,FOO,CC#B"]
print(solution(m,mi))
