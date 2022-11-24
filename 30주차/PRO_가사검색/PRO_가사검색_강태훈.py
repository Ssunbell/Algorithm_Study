
class Node:
    def __init__(self, key, data=0):
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
            curr = curr.child[char]
        curr.data += 1

    def regression(self, string):
        curr = self.root
        for idx,char in enumerate(string):
            if char in curr.child:
                curr=curr.child[char]
            else:
                break
        return curr, idx


def dfs(node, duration, answer=0):
    if duration==0:
        return answer + node.data
    if not node.child:
        return 0
    for nnode in node.child:
        answer += dfs(node.child[nnode],duration-1,answer)
    return answer

    
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
        answer.append(dfs(node, duration=len(log)-idx))
    print(answer)

print(solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],	["fro??", "????o", "fr???", "fro???", "pro?"]
))