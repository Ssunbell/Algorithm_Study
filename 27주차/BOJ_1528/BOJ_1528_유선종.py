from collections import deque

n = input()

def make_case(n, m):
    q = deque([])
    for i in range(2,2**(m+1)):
        case = format(i, 'b')
        num = int(case[1:].replace('0', '4').replace('1','7'))
        if num < n:
            q.append(num)
            
    return q
        
m = len(n)
n = int(n)
cases = make_case(n,m)
dp = deque([0])
for i in range(1,n):
    cnt=100
    for c in cases:
        if c <= i and dp[i-c] < cnt:
            cnt=dp[i-c]
    dp.append(cnt+1)
    
def bfs(n,l):
    if n==0:
        return l
    limit = 100
    g=-1
    for c in cases:
        if c <= n and dp[n-c] < limit:
            limit, g = dp[n-c], c
    if limit == 100:
        return [-1]
    else:
        return bfs(n-g,l+[g])
print(' '.join(map(str,sorted(bfs(n,[])))))