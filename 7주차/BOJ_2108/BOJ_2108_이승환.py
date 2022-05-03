import sys
n = int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

avg = int(round(sum(num) / n,0))

sorted_num = sorted(num)
mid = sorted_num[int(n/2)]

dict_num = {}
for i in sorted_num:
    if i not in dict_num:
        dict_num[i] = 1
    else:
        dict_num[i] += 1
val_dict = list(dict_num.values())
max_val = max(val_dict)
max_list = []
for i,j in dict_num.items():
    if j == max_val:
        max_list.append(i)
set_max = set(max_list)
if len(set_max) > 1:
    del_num = min(set_max)
    set_max.remove(del_num)
most = min(set_max)
    
ran = max(num) - min(num)

print(avg)
print(mid)
print(most)
print(ran)
