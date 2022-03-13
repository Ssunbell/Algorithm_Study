def solution(s):
    answer = 0

    word_num = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

    for i in word_num:
        s = s.replace(i,str(word_num[i]))

    answer = int(s)

    return answer

s = "one2threeonefour6"

print(solution(s))
