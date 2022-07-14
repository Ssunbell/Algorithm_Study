from collections import deque

def solution(n, info):
    answer = []
    
    # dfs로 완전탐색
    # (10,0) 이면 10점과녁을 안맞힘, (10,1)이면 10점 과녁을 맞힘
    # root는 (10,0),(10,1) 두개가 들어감
    st = deque()
    st.append((10,1))
    st.append((10,0))
    
    score_diff = -99999
    lion_cant_win = False
    lions_target = deque()
    lions_arrow = n
    lions_score = [0] * len(info)

    while st:
        curr,arrow = st.pop()
        
        if curr != 0:
            lions_target.append(arrow)
            st.append((curr-1,1))
            st.append((curr-1,0))
        else: # 마지막 요소일 경우 점수계산을 해야함
            for i in range(len(info)):
                if lions_target[i] == 1: # 라이언이 10-i 점수 과녁판을 맞힐경우
                    lions_arrow -= (info[i]+1)
                    # 여기서 추가로 lions_arrow == 0 이 되는 경우랑
                    # lions_arrow < 0 이되는 경우를 나누어서 생각해봐야함
                    lions_score[i] = (info[i]+1) * (10-i) # 라이언이 그 과녁을 이기기 위해 맞혀야 하는 점수
    
    return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

solution(n,info)