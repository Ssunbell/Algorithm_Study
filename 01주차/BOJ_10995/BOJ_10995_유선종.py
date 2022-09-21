iter = int(input())

for i in range(1, 1 + iter):
    if i%2 == 1:
        star = ' '.join(list('*' * iter))
        print(star)
    elif i%2 == 0:
        star = ' '.join(list('*' * iter))
        print(' ' + star)

#################################

iter = int(input())
line = "* " * iter

for i in range(iter):
    print(line)
    line = line[::-1]