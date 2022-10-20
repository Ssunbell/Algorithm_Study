def bi_gram(target:str, word:str) -> int:
    for cnt in range(1, len(target)):
        if (target[:cnt] != word[:cnt]):
            return cnt
        
    return len(target)

def tri_gram(left_word:str, target:str, right_word:str) -> int:
    for cnt in range(1, len(target)):
        if (target[:cnt] != left_word[:cnt]) and (target[:cnt] != right_word[:cnt]):
            return cnt

    return len(target)
    
def solution(words:list) -> int:
    words.sort()
    cnt = bi_gram(target=words[0], word=words[1])
    if len(words) > 2:
        cnt += bi_gram(target=words[-1], word=words[-2])
    for idx in range(1, len(words)-1):
        cnt += tri_gram(words[idx-1], words[idx], words[idx+1])

    return cnt