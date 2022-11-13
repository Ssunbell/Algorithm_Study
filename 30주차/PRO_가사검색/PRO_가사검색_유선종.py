'''
아이디어 : 트리 구조를 사용하되
           가사의 단어 길이(len)에 따라 트리를 따로 만들어줘서
           단어 길이가 같은 단어로만 구성된 트리를 만들어줌
           해당 트리에서 ?를 만나기 전의 count를 구해주면 됨
'''

class Node():
    def __init__(self, data):
        self.data = data
        self.child = {}
        self.count = 0

class Trie():
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, word:str):
        curr = self.root # 초기화했을 때의 데이터만 들어감, 여기서는 {}만 들어감
        curr.count += 1
        
        for char in word:
            if char not in curr.child:
                curr.child[char] = Node(char)
            curr = curr.child[char]
            curr.count += 1
                
    def search(self, word:str):
        node = self.root
        word = word.replace('?','')
        for char in word:
            if char not in node.child:
                return 0
            node = node.child[char]

        return node.count

def solution(words, queries):
    answer = []
    
    trie_dict = {}
    for word in words:
        if len(word) not in trie_dict:
            trie_dict[len(word)] = [Trie(), Trie()] # 순전파, 역전파
        
        trie_dict[len(word)][0].insert(word)
        trie_dict[len(word)][1].insert(word[::-1])
        
    for q in queries:
        if q.endswith('?'):
            if len(q) in trie_dict:
                answer.append(trie_dict[len(q)][0].search(q))
            else:
                answer.append(0)
        elif q.startswith('?'):
            if len(q) in trie_dict:
                answer.append(trie_dict[len(q)][1].search(q[::-1]))
            else:
                answer.append(0)

    return answer