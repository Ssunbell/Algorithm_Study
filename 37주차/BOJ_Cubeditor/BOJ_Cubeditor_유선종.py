def sub_string(string):
    table = [0] * len(string)
    j = 0
    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = table[j - 1]
            
        if string[i] == string[j]:
            j += 1
            table[i] = j
    return table

s = input()
answer = 0
for i in range(len(s)):
    answer = max(answer, max(sub_string(s[i:])))
    
print(answer)

# def sub_string(s:str):
#     l = len(s)
#     for length in range(l, 0, -1):
#         for start_idx in range(l - length + 1):
#             case = s[start_idx:length+start_idx]
#             cnt = 0
#             for i in range(l - length + 1):
#                 if case == s[i:length+i]:
#                     if not cnt:
#                         cnt += 1
#                     else:
#                         return length
#     return 0

# print(sub_string(input()))