import sys
input = sys.stdin.readline

# 이동방향에 대한 좌표변화
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def solve(n, m, k, fireballs):
    """_summary_

    Args:
        n (int): 격자의 가로, 세로 길이
        m (int): 초기 파이어볼의 개수
        k (int): Simulation 횟수
        fireballs (m x 5 matrix, columns = [r,c,m,s,d]): 파이어볼 정보를 담은 2차원 행렬
            [r,c,m,s,d]
            = [row_index, column_index, mass, speed, direction]를 의미

    Returns:
        int: k번 명령 후, 남아있는 파이어볼 질량의 합
    """
    for _ in range(k):
        # n_state : 현재 상태, 딕셔너리 형태로 key는 좌표, value는 해당 좌표에 위치한 파이어볼들을 리스트 형태로 저장
        n_state = {}
        for fireball in fireballs:
            r, c, m, s, d = fireball
            # d방향으로 s만큼 이동함 -> current_location + d_[d]*s
            nr, nc = (r-1+dr[d]*s)%n, (c-1+dc[d]*s)%n
            if (nr,nc) in n_state:
                n_state[(nr,nc)].append(fireball)
            else:
                n_state[(nr,nc)] = [fireball]
        # new_fireballs : 시뮬레이션 사이클이 진행된 후 생성된 fireball을 2 dim metrix로 저장
        new_fireballs = []
        # n_state의 key, value에 대하여 반복 (파이어볼 좌표와, 해당 좌표에 존재하는 파이어볼들에 대하여)
        for (r, c), loc_fireballs in n_state.items():
            r, c = r+1, c+1
            size = len(loc_fireballs)
            # 해당 좌표에 존재하는 파이어볼이 1개면 이동만 진행
            if size == 1:
                _, _, m, s, d = loc_fireballs[0]
                new_fireballs.append([r,c,m,s,d])
                continue
            # 해당 좌표에 존재하는 파이어볼이 2개 이상인 경우엔 이동 후 나뉘어짐
            elif size > 1:
                # r, c, m, s, d별로 구분하여 따로 저장. 예를들어 loc_info[2] 는 m에대한 정보만 리스트로 담겨져 있음
                loc_info = list(zip(*loc_fireballs))
                # 파이어볼이 나뉘어질 때 각 파이어볼의 질량, 속력, 방향
                sum_m, sum_s, sum_d = sum(loc_info[2])//5, sum(loc_info[3])//size, len(set(list(map(lambda x:x%2,loc_info[4]))))==1
                # 나뉘어진 질량이 0보다 큰 경우에만 파이어볼 생성
                if sum_m > 0:
                    # 모두 홀수거나 짝수면 sum_d==1, 그 외 0 => 각각 (0,2,4,6), (1,3,5,7)
                    for nd in (0,2,4,6) if sum_d==1 else (1,3,5,7):
                        new_fireballs.append([r, c, sum_m, sum_s, nd])
        # 차기 loop를 돌 땐 기존의 fireballs가 new_fireballs로 대치됨
        fireballs = new_fireballs
    # k번의 반복이 끝난 후, 남아있는 fireballs의 m만 뽑아 합을 구함
    return 0 if not fireballs else sum(list(zip(*fireballs))[2])
                
if __name__=="__main__":
    n, m, k = map(int, input().split())
    print(solve(n, m, k, [list(map(int, input().split())) for _ in range(m)]))