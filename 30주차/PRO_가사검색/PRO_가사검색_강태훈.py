class Node:
    def __init__(self, key, data=[]):
        self.key=key
        self.data=data
        self.child={}


class Trie:
    def __init__(self):
        self.root=Node(None)
    
    def insert(self, string):
        curr = self.root
        for char in string:
            if char not in curr.child:
                curr.child[char]=Node(char)
            curr.data.append(len(string))
            curr = curr.child[char]

    def regression(self, string):
        curr = self.root
        for idx,char in enumerate(string):
            if char == "?":
                return curr, idx
            if char in curr.child:
                curr=curr.child[char]
            else:
                break
        return curr, idx

    
def solution(words, queries):
    trie=Trie()
    trie_reverse=Trie()
    answer = []
    for word in words:
        trie.insert(word)
        trie_reverse.insert(word[::-1])
    for log in queries:
        if log.startswith("?"):
            node, idx = trie_reverse.regression(log[::-1])
        else:
            node, idx = trie.regression(log)
        answer.append(node.data.count(len(log)))
    print(answer)

print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]
))