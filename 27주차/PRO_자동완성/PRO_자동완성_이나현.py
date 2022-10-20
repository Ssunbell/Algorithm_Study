class Trie():
    def __init__(self):
        self.child = dict()
        self.count = 0
    def insert(self,string):
        curr = self
        for str in string:
            if str not in curr.child:
                curr.child[str] = Trie()
            curr = curr.child[str]
            curr.count += 1
    def search(self,string):
        curr = self
        for index, str in enumerate(string):
            if curr.child[str].count == 1 :
                return index + 1
            curr = curr.child[str]
        return index + 1
    def __str__(self):
        return str(self.child)+' '+str(self.count)
    
def solution(words):
    answer = 0
    word_dict = Trie()
    for word in words:
        word_dict.insert(word)
    for word in words:
        answer += word_dict.search(word)
    return answer

print(solution(["get", "abcde", "12345"]))
print(solution(["go", "gone", "guild"]))