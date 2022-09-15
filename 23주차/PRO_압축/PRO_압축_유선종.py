vocab = {'A':1, 'B':2, 'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,
        'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def solution(msg):
    answer = []
    if msg in vocab:
        return answer + [vocab[msg]]
    
    i = 0
    check = ''
    dict_num = 27
    
    while i < len(msg):
        check += msg[i]
        if check in vocab: # w를 찾는 과정
            i+=1
        else:
            vocab[check] = dict_num # w+c에 해당하는 단어 사전 등록
            dict_num += 1
            answer.append(vocab[check[:-1]]) # w의 출력값 answer에 추가
            check = ''
    answer.append(vocab[check])
    return answer