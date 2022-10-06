def solution(books,n,m):
    books = sorted(books,key=abs)
    len_walk = []
    neg = []
    pos = []

    while books:
        curr = books.pop()
        
        if curr < 0:
            neg.append(curr)
        else:
            pos.append(curr)

        if len(pos) == m:
            len_walk.append(abs(max(pos)))
            pos = []
        if len(neg) == m:
            len_walk.append(abs(min(neg)))
            neg = []

    if not neg:
        neg_val = 0
    else:
        neg_val = abs(min(neg))
    
    if not pos:
        pos_val = 0
    else:
        pos_val = abs(max(pos))

    if not len_walk:
        max_len = max(pos_val, neg_val)
    else:
        max_len = max(len_walk)

    answer = (sum(len_walk)*2) - max_len + ((pos_val + neg_val)*2)

    return answer

n,m = map(int,input().split())
books = list(map(int,input().split()))

print(solution(books,n,m))

# inp = [[7,2,[-37,2,-6,-39,-29,11,-28],131],
#        [8,3,[-18,-9,-4,50,22,-26,40,-45],158],
#        [6,2,[3,4,5,6,11,-1],29],
#        [1,50,[1],1]]
# i = 0
# for inpu in inp:
#     n,m,books,ans = inpu
#     result = solution(books,n,m)
#     i += 1
#     print(f"case {i}")
#     if result == ans:
#         print(f"정답 : {ans}")
#     else:
#         print(f"땡!, 나의 답 : {result}")

'''
1. 음수거리는 음수끼리, 양수는 양수끼리 가야한다
   왜냐하면 음수를 갔다가 양수를 가면 어차피 0을 들리기 때문.
   즉 음수를 가면 그 다음에 음수를 간다. 양수를 가면 그 다음에 양수를 간다.
2. 가장긴 거리, 즉 절대값이 가장 긴 거리는 마지막에 방문한다.
   거기를 갈 때 책을 최대한 들고가서 떨궈준다.
3. 가장 긴 거리부터 최대치 책의 개수만큼 빼준다.

1. 절대값 순서로 정렬
2. 절대값 순서로 저장, 그 뒤로 양수면 양수만, 음수면 음수만 책을 들고갈 수 있는 개수만큼 묶음
3. 묶인 책중에서 가장 큰값들만 저장, 저장된 원소중 가장 큰 값은 그대로 더하고 나머지는 x2해서 더함
예) -39, -37, -29, -28, 11,-6, 2 순서라면
    -39를 뽑아서 neg에 저장
    -37을 뽑아서 neg에 저장, neg의 길이가 2이므로 len_walk.append(max(abs(neg))), neg = []
    -29를 뽑아서 neg에 저장,
    -28을 뽑아서 neg에 저장, neg의 길이가 2이므로 len_walk.append(max(abs(neg))), neg = []
     11을 뽑아서 pos에 저장,
     -6을 뽑아서 neg에 저장,
     2를 뽑아서 pos에 저장, len(pos) == 2이므로 len_walk.append(max(abs(pos))), pos = []
     max_len = max(len_walk)
     answer = (sum(len_walk)*2) - max_len + ((max(abs(pos)) + max(abs(neg)))*2)
'''
