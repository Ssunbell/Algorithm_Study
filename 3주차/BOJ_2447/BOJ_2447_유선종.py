n = int(input())

square = 0
while n:
    n = n // 3
    square += 1
square = square -1
star = '*\n'

def count_star(square,star):
    if square == 0:
        print(star)
        return

    star = star
    sl = [star for _ in range(9)]
    temp_result = []
    for i in range(0,9,3):
        temp = []
        sl1 = sl[i].replace('\n', ',').split(',')
        sl3 = sl[i+2].replace('\n', ',').split(',')
        if i == 3:
            sl2 = sl[i+1].replace('*', ' ')
            sl2 = sl2.replace('\n', ',').split(',')
        else:
            sl2 = sl[i+1].replace('\n', ',').split(',')
        sl1.pop()  ## 계행을 쉼표로 바꾸고 스플릿하면 마지막에 빈 공간이 생기므로 pop으로 빈공간 제거
        sl2.pop()
        sl3.pop()
        for x,y,z in zip(sl1, sl2, sl3):
            line = [x+y+z + '\n']
            temp.extend(line)
        temp_result.append(''.join(temp))
    star = temp_result[0] + temp_result[1] + temp_result[2]
    square -= 1
    count_star(square, star)

############################################################

count_star(square, star)
