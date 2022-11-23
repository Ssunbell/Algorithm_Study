"""
아이디어:
    나이브 구현으로는 O(N^2)이 소요되기 때문에, O(NlogN)이하로 구현해야함
    따라서 매 쿼리마다 "검색 키워드" 조건에 맞는 개수를 O(logN)이하로 구현해야함.
    "검색 키워드" 조건에 맞는 개수는 이분탐색을 이용해서 해결 가능함.
    1. words의 각 word의 길이를 index로 갖는 list 생성
    2. 검색 쿼리에 해당하는 개수를 이분탐색으로 구현
        # 참고: 
            bisect_left(x, a):
                찾고자하는 a가 list x에 포함되어 있다면, x에서의 a의 index 반환
                찾고자하는 a가 list x에 포함되어 있지 않다면, 오름차순으로 x에서 a를 삽입할 index 반환
            bisect_right(x, a):
                찾고자하는 a가 list x에 포함되어 있다면, x에서의 a의 index + 1 반환
                찾고자하는 a가 list x에 포함되어 있지 않다면, 오름차순으로 x에서 a를 삽입할 index 반환
        2-1. left_index = bisect_left(같은 word 길이를 갖는 list, "?"를 a"로 replace한 단어)
        2-2. right_index = bisect_right(같은 word 길이를 갖는 list, "?"를 z"로 replace한 단어)
        2-3. 해당 검색 쿼리에 해당하는 개수 = right_index - left_index
    3. 쿼리마다 2번 과정에 해당하는 "해당 검색 쿼리에 해당하는 개수"를 append
"""
from bisect import bisect_left, bisect_right
def solution(words, queries):
    answer = []
    # arr[i]: 길이가 i인 word들이 담겨져 있는 배열
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    for query in queries:
            # ????o -> "aaaao", "zzzzo" -> 무조건 arr의 양끝에 위치함
            # 따라서 [::-1]로 반전시켜야함.
            # 따라서 reversed_arr를 따로 만들어줘서 oaaaa, ozzzz를 활용할 수 있도록함
            # ["emarf", "oakak", "odorf", "tnorf", "tsorf"] -> 여기서 "oaaaa", "ozzzz"의 위치를 찾으면 됨
        if query[0] == "?":
            left_index = bisect_left(reversed_arr[len(query)], query.replace("?", "a")[::-1])
            right_index = bisect_right(reversed_arr[len(query)], query.replace("?", "z")[::-1])
        else:
            left_index = bisect_left(arr[len(query)], query.replace("?", "a"))
            right_index = bisect_right(arr[len(query)], query.replace("?", "z"))
        answer.append(right_index - left_index)
    return answer

# 효율성 통과 못한 코드
def _solution(words, queries):
    answer = []
    """
    나이브 구현:
        1. 물음표 개수를 센다. (count)
        2. 가장 우선적으로 쿼리와 비교하려는 단어와 길이가 같은지부터 확인
            2-1. ?가 맨 오른쪽에 있는 경우:
                l = len(쿼리) - 물음표_개수
                for문으로 words의 단어들 중에 쿼리[:l]과 일치하는지 확인
            2-2. ?가 맨 왼쪽에 있는 경우:
                l = 물음표_개수
                for문으로 words의 단어들 중에 쿼리[l:]과 일치하는지 확인
    """
    for q in queries:
        res = 0
        for w in words:
            if len(q) == len(w):
                cnt_wildcard = q.count("?")
                if q[-1] == "?" and w[:len(w) - cnt_wildcard] == q[:len(w) - cnt_wildcard]:
                    res += 1
                elif q[0] == "?" and w[cnt_wildcard:] == q[cnt_wildcard:]:
                    res += 1
        answer.append(res)
    return answer