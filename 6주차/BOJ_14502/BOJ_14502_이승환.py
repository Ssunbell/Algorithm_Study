# n,m = map(int,input().split())
# lab = [list(input().split()) for _ in range(n)]

def zero_index(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                result.append([i,j])
    return result

def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []
    # 2.
    def generate(chosen):
        if len(chosen) == r:
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

def make_wall(arr):
    result = []
    for i in range(len(arr)):
        lab_copy = [item[:] for item in lab]
        for j in range(len(arr[i])):
            lab_copy[arr[i][j][0]][arr[i][j][1]] = 1
        result.append([item[:] for item in lab_copy])
    return(result)

# 2차원배열을 받아서 2차원배열로 출력
# 바이러스가 퍼지는 것을 구현해야함.
def virus(arr):
    return arr

def find_zero(arr):
    sum_zero = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                sum_zero += 1
    return sum_zero

lab = [[2,0,0],[0,0,1]]

zero_idx = zero_index(lab)
comb_zero = combination(zero_idx,3)
wall_lab = make_wall(comb_zero)
lab_result = []
for i in wall_lab:
    lst = virus(i)
    lab_result.append(find_zero(lst))

print(lab_result)

