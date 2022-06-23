import sys
input = sys.stdin.readline

s = list(input().rstrip())[::-1]

def cal(start):
    r = 0
    while s:
        a = s.pop()
        if a == "(" or a == "[":
            r += cal(a)
        elif start == "(" and a == ")":
            return 2 * max(1,r)
        elif start == "[" and a == "]":
            return 3 * max(1,r)
    
    # 리스트가 비었는데 최종 return 하지 못했다는 것은 괄호에 문제가 있음을 의미
    print(0)
    sys.exit()

ans = 0    
while s:
    ans += cal(s.pop())
print(ans)

# list_bracket = [i for i in input()]
# print(list_bracket)
# cnt = 0
# def find_bracket():
#     s = []
#     result = []
#     global cnt
#     while list_bracket:
#         print(result, s)
#         t = list_bracket.pop(0)
#         if len(s)>0:
#             if s[-1] == '[' and t == ')' or s[-1] == ']' and t == '(':
#                 return 0
            
#             if s[-1] == '(' and t == ')':
#                 result.append(2)
#                 s.pop()
#                 try:
#                     if s[-1] == '(' or s[-1] == '[':
#                         result.append('*')
#                 except:
#                     while result:
#                         print(cnt)
#                         num = result.pop(0)
#                         if num == '*':
#                             num2 = result.pop(0)
#                             cnt *= num2
#                         else:
#                             cnt += num
                
                    
#             elif s[-1] == '[' and t == ']':
#                 result.append(3)
#                 s.pop()
#                 try:
#                     if s[-1] == '(' or s[-1] == '[':
#                         result.append('*')
#                 except:
#                     while result:
#                         print(cnt)
#                         num = result.pop(0)
#                         if num == '*':
#                             num2 = result.pop(0)
#                             cnt *= num2
#                         else: 
#                             cnt += num
#             else:
#                 s.append(t)
#         else:
#             s.append(t)
            
#     return result

# print(find_bracket())
"""
[()[()]]
[, [(, [ [[ [[( [[
0  0   2  0  0   0
0  0   1  1  1   1
"""