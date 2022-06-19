import sys

input = lambda: sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    list_imp = list(map(int, input().split()))
    count = 0
    while list_imp:
        max_imp = max(list_imp)
        p = list_imp.pop(0)
        if p < max_imp:
            list_imp.append(p)
            m = (m - 1) % len(list_imp)
        else:
            count += 1
            if m == 0:
                print(count)
                break
            m = (m - 1) % len(list_imp)


'''              
1 2 3 4 - 2
2 3 4 1 - 1
3 4 1 2 - 0
4 1 2 3 - (-1 % 4) = 3
1 2 3 - (-1 % 3) = 2
2 3 1 - (-2 % 3) = 1
3 1 2 - (-3 % 3) = 0
1 2
'''