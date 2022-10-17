class Node:
    def __init__(self, key, data=[]):
        self.key = key
        self.child = {}
        self.data = []

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        cur = self.root
        for token in word:
            cur.data.append(word)
            if token not in cur.child:
                cur.child[token] = Node(token)
            cur = cur.child[token]
        cur.data.append(word)

    def goto(self, word):
        cur = self.root
        for token in word:
            cur = cur.child[token]
        return cur

    def auto_build(self, word):
        for i in range(1, len(word)):
            child = self.goto(word[:i]).data
            if len(child) == 1:
                return i
        return len(word)


def solution(words):
    trie = Trie()
    answer = 0
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.auto_build(word)
    return answer
