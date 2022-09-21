n, m = map(int,input().split())

lst = [i for i in range(1,n+1)]

# 순열을 이용하여 구현
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    result = []
    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            result.append(chosen[:])
            return
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return result

k = permutation(lst,m)

k = sorted(k)

for i in k:
    print(" ".join(map(str,i)))
