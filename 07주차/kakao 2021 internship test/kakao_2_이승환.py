places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

def solution(places):
    answer = []
    
    def place_expand(place):
        room = ["XXXXXXX"]
        for line in place:
            add_line = "X"+line+"X"
            room.append(add_line)
        room.append("XXXXXXX")
        return room

    def check_nodes(place,i,j,depth,x=None,y=None, chk = 1):
        if depth == 2:
            return chk
        depth += 1
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        if place[i][j] == "P" or depth == 2:
            for idx in range(4):
                if -dx[idx] == x and -dy[idx] == y:
                    continue
                if place[i+dx[idx]][j+dy[idx]] == "X":
                    continue
                elif place[i+dx[idx]][j+dy[idx]] == "P":
                    chk = 0
                    return chk
                else:
                    chk = check_nodes(place,i+dx[idx],j+dy[idx],depth,dx[idx],dy[idx])
                    if chk == 0:
                        return chk
        return chk

    def solution(place):
        place_check = [[0]*5 for _ in range(5)]
        for i in range(1,6):
            for j in range(1,6):
                chk = check_nodes(place,i,j,0)
                place_check[i-1][j-1] = chk
        pc = sum(place_check, [])
        if 0 in pc:
            ans = 0
        else:
            ans = 1
        return ans

    for place in places:
        new_place = place_expand(place)
        answer.append(solution(new_place))
        
    return answer