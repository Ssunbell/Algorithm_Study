n, m = map(int, input().split())

dict_num = {input() : str(i) for i in range(1, n+1)}

reverse_dict = dict(map(reversed, dict_num.items()))

for j in range(m):

    pokemon = input()

    if pokemon in dict_num.keys():
        print(dict_num[pokemon])
    else:
        print(reverse_dict[pokemon])