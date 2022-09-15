n,r,c = map(int,input().split())

# 영역을 나누는 기준 : first_idx + 2^((n-1)*2)*idx

# 맨 처음에 idx 는 (0,0)이므로 0
first_idx = 0
# n==0 이면 한칸이고 영역을 찾은것이기에 종료
while n != 0:
    # 좌표가 어디에 있는지 확인
    if 0<= r <pow(2,n-1) and 0<= c <pow(2,n-1):
        idx = 0
    elif 0<= r <pow(2,n-1) and pow(2,n-1)<= c <pow(2,n):
        idx = 1
    elif pow(2,n-1)<= r <pow(2,n) and 0<= c <pow(2,n-1):
        idx = 2
    elif pow(2,n-1)<= r <pow(2,n) and pow(2,n-1)<= c <pow(2,n):
        idx = 3

    first_idx += pow(2,(n-1)*2) * idx  
    r = r%pow(2,n-1)
    c = c%pow(2,n-1)
    n -= 1

print(first_idx)