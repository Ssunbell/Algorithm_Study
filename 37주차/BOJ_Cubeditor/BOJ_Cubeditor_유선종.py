

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