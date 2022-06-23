from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    # 중복 신고 제거
    report = list(set(report))

    # user별 신고한 id 
    user = defaultdict(set)
    
    # user별 신고 당한 횟수 저장
    count = defaultdict(int)
    
    for i in report:
        # report의 첫번째 값은 신고자 id, 두번째 값은 신고당한 id
        reporter, reported = i.split()
        
        # 신고자가 신고한 id 추가
        user[reporter].add(reported)
        
        # 신고당한 id의 신고 횟수 추가
        # 이렇게 하는 이유: 같은 사람이 같은 사람 신고하면 어차피 횟수는 1번만 증가해야하기 때문데
        count[reported] += 1

    # k번 이상 신고 당했으면, 받을 메일 추가
    for j in id_list:
        result = 0
        for z in user[j]:
            if count[z] >= k:
                result += 1
        answer.append(result)
    return answer