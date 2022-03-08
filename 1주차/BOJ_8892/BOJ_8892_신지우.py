T = int(input())

for i in range(T):
    k = int(input())
    k_list = [input() for i in range(k)]
    password = 0
    for j in range(k):
        for z in range(j+1, k):
            password1 = k_list[j] + k_list[z]
            password2 = k_list[z] + k_list[j]
            if password1 == password1[::-1]:
                password = password1
            if password2 == password2[::-1]:
                password = password2
    print(password)