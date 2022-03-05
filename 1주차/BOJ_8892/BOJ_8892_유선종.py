t = int(input())

for case in range(t):
    k = int(input())
    storage = [input() for i in range(k)]
    pald_exist = 0
    
    for i in range(len(storage)):
        for j in range(len(storage)):
            if i != j:
                pald = storage[i] + storage[j]
                if pald == pald[::-1]:
                    pald_exist = pald

    if bool(pald_exist) == True:
        print(pald_exist)
    else:
        print(pald_exist)