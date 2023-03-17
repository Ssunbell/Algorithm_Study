#백준 1701_Cubeditor
# KMP
# 파이 배열 만들기
def make_table(string):
    l = len(string)
    table = [0] * l
    j = 0
    for i in range(1, l):
        while j > 0 and string[i] != string[j]:
            j = table[j-1]
        if string[i] == string[j]:
            table[i] = j + 1
            j += 1
    return table

def cubeditor(string):
    l = len(string)
    answer = 0
    for i in range(l):
        table = make_table(string[i:])
        answer = max(answer, max(table))
    return answer

print(cubeditor(input()))

# 시간초과 : bfs
# from collections import deque
# input_string = input()
# que = deque([input_string])
# pieces = set()
# l = len(que)
# while que:
#     string = que.popleft()
#     if l != len(string):
#         l = len(string)
#         pieces = set()
#         piece = string[:-1]
#         pieces.add(piece)
#         que.append(piece)
#     piece = string[1:]
#     if piece in pieces:
#         print(len(piece))
#         break
#     pieces.add(piece)
#     que.append(piece)

# else:
#     print(0)


# 메모리 초과 : dp
# input_string = input()
# dp = set()
# answer = 0
# for i in range(len(input_string)): #stride
#     string = ''
#     for j in range(i,-1,-1):
#         string += input_string[j]
#         if string in dp:
#             answer = max(answer, len(string))
#         dp.add(string)
# print(answer)