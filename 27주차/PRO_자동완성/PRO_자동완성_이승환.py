class trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        curr = self.root
        for c in s:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["*"] = s
    
    def search(self, s):
        curr = self.root
        word_len = 0
        depth = 0
        for c in s:
            depth += 1
            if len(curr[c]) > 1:
                word_len = depth
                curr = curr[c]
            else:
                curr = curr[c]
                if depth == len(s):
                    word_len += 1
        return word_len

def solution(words):
    trie_ = trie()
    for word in words:
        trie_.insert(word)

    answer = 0
    for word in words:
        answer += trie_.search(word)

    return answer

# 시간초과로 실패,,,,
# '''
# word1은 찾고자하는 단어, word2는 비교하는 단어이다.
# 1. word1의 길이가 더 긴 경우, 최대 word2의 길이만큼만 비교가 가능하다.
#    word2의 마지막 자리까지 비교를 하고 sim += 1 을 했다면, 
#    len(word2)만큼 같은 단어라는 이야기이고, 두 단어가 다른 단어로 구분되려면
#    len(word2)+1 만큼 입력을 해야한다. 이때 sim = len(word2)
#    만약 그 이전에 끝났다면 비교했던 부분까지(sim만큼) 같은 단어가되는것이고
#    sim += 1을 하면 입력해야하는 문자의 수가 된다.
# 2. word2의 길이가 더 길거나 같은 경우, 최대 word1까지의 길이만큼만 비교가 가능하다.
#    이때 1번의 경우와 같지만 word1의 마지막까지 비교할 필요가 없다.
#    len(word1)-1 까지만 비교한 후 두 단어가 같다면 마지막에 한글자를 더 입력해주면 된다.
# 3. 즉, 1번의 경우 range(1,len(word2)+1) 만큼 비교를 하고
#    2번의 경우 range(1,len(word1)) 만큼 비교를 한다.
#    입력해야 하는 단어의 수는 최종적으로 나온 sim + 1을 해주면 된다.
# 4. 그 후 모든 단어를 비교해보며 입력해야 하는 단어의 수를 구한다.
# '''
# def sim_check(word1,word2):
#     sim = 0
#     if len(word1) > len(word2):
#         for i in range(1,len(word2)+1):
#             if word1[:i] == word2[:i]:
#                 sim += 1
#             else:
#                 break
#     else:
#         for i in range(1,len(word1)):
#             if word1[:i] == word2[:i]:
#                 sim += 1
#             else:
#                 break
#     return sim+1

# def solution(words):
#     answer = 0
#     for word1 in words:
#         max_sim = 0
#         for word2 in words:
#             if word1 == word2:
#                 continue
#             max_sim = max(max_sim,sim_check(word1,word2))
#         answer += max_sim
#     return answer

words = [[["go","gone","guild"],7],
        [["abc","def","ghi","jklm"],4],
        [["word","war","warrior","world"],15]]


i = 0
for word in words:
    w,ans = word
    result = solution(w)
    i += 1
    if result == ans:
        print(f"test case {i} 정답")
    else:
        print(f"test case {i} 땡!\n나의답 : {result}, 정답 : {ans}")
