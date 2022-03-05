testcase_num = int(input())

for i in range(testcase_num):
    pal = 0
    word_num = int(input())
    arr = [input() for j in range(word_num)]

    for j in range(len(arr)):
        for k in range(1, len(arr)-j):
            string = arr[j] + arr[j+k]
            if(string[::-1] == string):
                pal = string
            string = arr[j+k] + arr[j]
            if(string[::-1] == string):
                pal = string
                
    print(pal)
