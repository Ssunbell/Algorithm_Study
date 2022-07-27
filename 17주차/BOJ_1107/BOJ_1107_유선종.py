target = int(input())
ans = abs(100 - target)
m = int(input())
if m: 
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001): 
    for n in str(num):
        if n in broken: 
            break
    else: 
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)

# n = input()
# m = int(input())
# if m != 0:
#     break_list = set(map(int,input().split()))
# else:
#     break_list = []
# num_list = [0,1,2,3,4,5,6,7,8,9]
# for num in break_list:
#     num_list.remove(num)

# if not num_list:
#     print(abs(int(n) - 100))
# else:
#     # +, -로만 이동
#     cnt0 = abs(int(n) - 100)
    
#     # 같은 자리 비교
#     start = ''
#     cnt = 0
#     for i in range(len(n)):
#         cnt += 1
#         num =  int(n[:i + 1])
#         tmp_list = []
#         for j in num_list:
#             denum = int(start[:] + str(j))
#             tmp_list.append(abs(num-denum))
            
#         if tmp_list.count(min(tmp_list)) == 1:
#             start += str(num_list[tmp_list.index(min(tmp_list))])
#         else: # min 값이 두개일 경우 그 다음 값으로 두 값중에 무엇을 선택할지 고름
#             try:
#                 if int(n[i+1]) < 5:
#                     start += str(num_list[tmp_list.index(min(tmp_list))])
#                 else:
#                     start += str(num_list[tmp_list.index(min(tmp_list))+1:][tmp_list.index(min(tmp_list))]) 
#             except:
#                 start += str(num_list[tmp_list.index(min(tmp_list))])
#     cnt += abs(int(n) - int(start))
    
#     # 다른 자리 비교 예) 999라면 1000, 100 라면 99
#     if 0 in num_list and len(num_list) != 1: # 0이 있을 경우에 맨 앞의 자리수는 0이 올 수 없음
#         start2 = str(num_list[1])
#         cnt2 = 1
#     elif 0 in num_list and len(num_list) == 1: # num_list 가 [0]일 경우에 굳이 할 필요가 없음
#         start2 = ''
#         cnt2 = 500000000
#     elif 0 not in num_list:
#         start2 = str(num_list[0])
#         cnt2 = 1
        
#     for _ in range(len(n)):
#         start2 += str(min(num_list))
#         cnt2 += 1

#     cnt2 += abs(int(start2) - int(n))
    
#     if len(n) > 1:
#         cnt3 = 0
#         start3 = ''
#         for _ in range(len(n)-1):
#             start3 += str(max(num_list))
#             cnt3 += 1
#         cnt3 += abs(int(n) - int(start3))
#         print(min(cnt0, cnt, cnt2, cnt3))
#     elif num_list == [0]:
#         print(min(cnt0, cnt, cnt2))
#     else:
#         print(min(cnt0, cnt, cnt2))