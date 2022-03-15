n, m = map(int, input().split())
un_listen = {input() : i for i in range(n)}
unseen_unlisten = []

for j in range(m):
    un_seen = input()
    if un_seen in un_listen:
        unseen_unlisten.append(un_seen)
        unseen_unlisten.sort()

print(len(unseen_unlisten), *unseen_unlisten, sep='\n')
