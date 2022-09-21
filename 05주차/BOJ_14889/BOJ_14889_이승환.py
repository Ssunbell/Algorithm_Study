n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]

def sum_capa(lst):
    capa = 0
    for i in lst:
        for j in lst:
            capa += s[i][j] + s[j][i]
    return int(capa/2)

team_mate = [i for i in range(n)]

def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []
    # 2.
    def generate(chosen):
        if len(chosen) == r:
            if 0 not in chosen:
                return
            result.append(chosen[:])
            return
    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
    return result
k = combination(team_mate,int(len(team_mate)/2))

result = []

for lst in k:
    lst2 = [i for i in range(n) if i not in lst]
    result.append(abs(sum_capa(lst) - sum_capa(lst2)))

print(min(result))

