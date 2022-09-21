n = int(input())

for i in range(n):
    k = int(input())
    words = [input() for i in range(k)]
    password = 0
    for j in range(k):
        for h in range(j+1, k):
            password1 = words[j] + words[h]
            password2 = words[h] + words[j]
            if password1 == password1[::-1]:
                password = password1
            if password2 == password2[::-1]:
                password = password2
    print(password)
