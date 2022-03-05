testcase_num = int(input())

for i in range(testcase_num):
    st_score = list(map(int, input().split()))
    st_num = st_score[0]
    score = st_score[1:]
    avg_score = sum(score) / st_num
    st_over_avg = 0
    for i in range(st_num):
        if score[i] > avg_score:
            st_over_avg += 1
    ratio = (st_over_avg/st_num)*100
    print("{:.3f}%".format(ratio))
