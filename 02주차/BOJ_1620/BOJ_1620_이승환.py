N, M = map(int,input().split())

pokemon_dict = {(i + 1) : input() for i in range(N)}
question = [input() for i in range(M)]
pokemon_reverse  = dict(map(reversed, pokemon_dict.items()))

for i in question:
    try:
        q = int(i)
        print(pokemon_dict[q])
    except ValueError:
        print(pokemon_reverse[i])


""" for i in question:
    try:
        q = int(i)
        print(poketmon_dict[q])
    except ValueError:
        for key,value in poketmon_dict.items():
            if value == i:
                print(key)
 """