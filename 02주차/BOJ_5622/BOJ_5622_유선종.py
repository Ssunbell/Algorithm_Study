dic = {
    2 : "ABC",
    3 : "DEF",
    4 : "GHI",
    5 : "JKL",
    6 : "MNO",
    7 : "PQRS",
    8 : "TUV",
    9 : "WXYZ"
}

call = list(input())
storage = [list(i) for i in dic.values()]
total = 0

for alp in call:
    for num in range(len(storage)):
        if alp in storage[num]:
            total += num + 3
print(total) 
