n = int(input())

cdn = [ list(map(int,input().split())) for i in range(n)]

cdn.sort()

for i in cdn:
    print(i[0],i[1])