def solution(n, info):
    answer = [0 for _ in range(11)]
    tmp = [0 for _ in range(11)] # 라이언이 화살 정보를 저장하기 위한 변수
    maxDiff = 0 
    # 비트단위시프트 연산자
    # 왼쪽 비트시프트(<<)가 될 때는 오른쪽에 0이 주어진 개수만큼 추가 ex) 10 << 1 = 10100 10진수로 20
    # 오른쪽 비트시프트(>>)가 될 때는 왼쪽에 0이나 1이 개수만큼 추가 가장 오른쪽에 있는 1비트는 사라짐 ex) 10 >> 1 = 101 10진수로 5

    for subset in range(1, 1 << 10): # 비트형으로 표현된 모든 부분 집합을 for돌리기
        ryan = 0
        apeach = 0
        cnt = 0

        for i in range(10): # i번째 원소가 부분집합에 존재하는지
            if subset & (1 << i): # i번째 원소가 subset에 존재한다면
                ryan += 10 - i # 라이언의 점수
                tmp[i] = info[i] + 1 # 라이언이 쏜 화살의 개수 어피치 보다 +1
                cnt += tmp[i] # 현재 라이언이 쏜 화살의 개수

            # 라이언이 이기지 않는 경우
            else:
                tmp[i] = 0 # 라이언은 화살을 안쏘면 됨!
                if info[i]: # 어피치가 1개라도 쏜 화살이 있으면 어피치에게 점수 부여
                    apeach += 10 - i

        if cnt > n:
            continue
        
        # 0점에 남은 화살 기록
        tmp[10] = n - cnt   

        # 점수가 같은 경우에도 낮은 점수를 맞힌 개수의 값을 출력해야하기 때문에 
        if ryan - apeach == maxDiff:
            for i in reversed(range(11)): # 0점부터 비교
                if tmp[i] > answer[i]: # 낮은 점수를 더 많이 맞힌 경우
                    maxDiff = ryan - apeach
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break
        # 점수차가 maxDiff보다 크면
        elif ryan - apeach > maxDiff:
            maxDiff = ryan - apeach
            answer = tmp[:] # 점수차가 가장 클 때의 화살 기록 

    # 라이언이 못이기는 경우
    if maxDiff == 0:
        answer = [-1]

    return answer