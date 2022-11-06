'''
아이디어 : 왼쪽부터 순회하여 딕셔너리에 보석을 넣은 뒤에,
           모든 보석이 다 들어오게 되면 그 길이를 구해서 갱신함
           갱신한 후 만약 해당 보석들 중에 **맨 왼쪽에** 있는 보석이 새로이 나타나게 되면
           맨 왼쪽의 보석을 버리고 새롭게 나타난 보석을 딕셔너리에 갱신해주고
           그 길이를 반환
'''

def solution(gems):
    # 보석 종류
    category_len = len(set(gems))

    # 보석 종류가 하나면 바로 종료
    if category_len == 1:
        answer = [1,1]
    else:
        answer = [1, len(gems)]
        gems_dict = {}
        left = 0
        right = 1
        # 가장 왼쪽에 있는 보석
        left_gem = gems[left]
        gems_dict[gems[left]] = left # 보석의 현재 위치 저장

        while right < len(gems):
            # 보석의 현재 위치 갱신
            gems_dict[gems[right]] = right
            if gems[right] == left_gem: # 만약에 맨 왼쪽에 있는 보석이 새롭게 들어왔다면
                new = sorted(gems_dict, key=lambda x: gems_dict[x])[0] # 그 다음 왼쪽 보석을 찾아서
                left_gem, left = new, gems_dict[new] # 맨 왼쪽 보석과 해당 위치를 갱신

            if len(gems_dict) == category_len:
                if answer[1]-answer[0] > right-left: # 만약 최솟값이라면 반환
                    answer = [left+1, right+1]

            right += 1
        
    return answer