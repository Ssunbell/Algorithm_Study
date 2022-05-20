import sys

input_s = lambda : sys.stdin.readline().strip()

photo = int(input_s())
std_num = int(input_s())
all_std = list(map(int,input_s().split()))

reco = [0]*photo
reco_num = [0]*photo
reco_oldest = [0]*photo
input_num = 0

for std in all_std:
    input_num += 1
    if std in reco:
        idx = reco.index(std)
        reco_num[idx] += 1
    elif 0 in reco:
        idx = reco.index(0)
        reco[idx] = std
        reco_num[idx] = 1
        reco_oldest[idx] = input_num
    else:
        if reco_num.count(min(reco_num)) > 1:
            min_list = list(filter(lambda x: reco_num[x] == min(reco_num), range(len(reco_num))))
            last_num = min([reco_oldest[idx] for idx in min_list])
            last_idx = reco_oldest.index(last_num)
            reco[last_idx] = std
            reco_num[last_idx] = 1
            reco_oldest[last_idx] = input_num
        else:
            idx = reco_oldest.index(min(reco_oldest))
            reco[idx] = std
            reco_num[idx] = 1
            reco_oldest[idx] = input_num

reco.sort()

result = []
for i in reco:
    if i != 0:
        result.append(i)

for i in result:
    print(i,end=" ")