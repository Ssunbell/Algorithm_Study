# 사진틀이랑 추천수 리스트 만들기
# 0번 인덱스는 바로 집어넣기
# 한 학생 추천 여러번 : 추천수만 올라가게
# 사진틀에서 학생 제외해야할 때 : 추천수 최소 구해주고 del (가장 첫번째를 삭제하므로 조건 성립)


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
recommends = list(map(int, input().split()))

photo = [recommends[0]]
recommends_num = [1]

for i in range(1, m):
    if recommends[i] in photo:
        for j in range(len(photo)):
            if photo[j] == recommends[i]:
                recommends_num[j] += 1
    else:
        if len(photo) >= n:
            for j in range(len(photo)):
                if recommends_num[j] == min(recommends_num):
                    del photo[j]
                    del recommends_num[j]
                    break
        photo.append(recommends[i])
        recommends_num.append(1)

photo.sort()
for p in photo:
    print(p, end=' ')
print()

# 30840kb 80ms
