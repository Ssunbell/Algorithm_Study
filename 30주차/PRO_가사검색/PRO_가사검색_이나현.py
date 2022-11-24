#[프로그래머스 - 가사검색] -> 마지막 한 케이스 시간초과
from collections import defaultdict

class Node(object):
    def __init__(self, key, end=False):
        self.key = key
        self.len = defaultdict(lambda:0)
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        curr = self.head
        l = len(word)
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node(w)
            curr.len[l] += 1
            curr = curr.children[w]
    
    def search(self, query):
        curr = self.head
        idx = 0
        cnt = 0
        l = len(query)
        for q in query:
            idx += 1
            if q in curr.children:
                curr = curr.children[q]
            elif q == '?':
                cnt = curr.len[l]
                break
            else:
                break
        if idx in curr.len:
            return cnt
        return cnt

def solution(words, queries):
    trie = Trie()
    inv_trie = Trie()
    answer = []
    for word in words:
        trie.insert(word)
        inv_trie.insert(word[::-1])
    for query in queries:
        if query[0] != '?':
            cnt = trie.search(query)
        else:
            cnt = inv_trie.search(query[::-1])
        answer.append(cnt)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))