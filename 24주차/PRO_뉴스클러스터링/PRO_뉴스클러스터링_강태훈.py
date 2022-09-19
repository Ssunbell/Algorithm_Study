from collections import Counter


def solution(str1, str2):
    def process(text): return Counter(filter(lambda x: x.isalpha(),
                                             [text[i:i+2].upper()for i in range(len(text) - 1)]))
    set1 = process(str1)
    set2 = process(str2)
    union_size = sum((set1 | set2).values())
    intersection_size = sum((set1 & set2).values())
    return 65536 if union_size == 0 else 65536 * intersection_size // union_size


tc = [["FRANCE", "french"
       ], ["handshake", "shake hands"
           ], ["aa1+aa2", "AAAA12"
               ], ["E=M*C^2", "e=m*c^2"
                   ]]
for c in tc:
    print(solution(*c))

'''
str1, str2로 만들어진 두 딕셔너리를 set1, set2에 저장 후 두 딕셔너리의 key를 union하여 집합 items에 저장한다.
교집합(set1&set2)의 모든 value를 더해 intersection_size에 저장한다.
합집합(set1|set2)의 모든 value를 더해 union_size에 저장한다.
자카드 유사도 (intersection_size / union_size)를 구하여 65536을 곱해 출력한다.
union_size가 0이면 65536을 출력한다.
'''
