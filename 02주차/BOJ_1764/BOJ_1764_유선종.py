n, m  = map(int, input().split())
dic = {input() : 0 for i in range(n)}

for i in range(m):
    name = input()
    if name in dic.keys():
        dic[name] = 1
        
del_name = [name for name, n in dic.items() if n == 0]
for name in del_name:
    del dic[name]

print(sum(dic.values()))
for i in sorted(dic):
    print(i)
