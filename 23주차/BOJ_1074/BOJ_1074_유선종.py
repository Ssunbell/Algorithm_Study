n, r, c = map(int, input().split())

answer = 0
while n != 0:
    n -= 1
    length = 2 ** n
    
    if r < length and c < length: # 1 사분면
        answer += 0
    
    elif r < length and c >= length: # 2 사분면
        answer += (4 ** n)
        c -= length
    
    elif r >= length and c < length: # 3 사분면
        answer += (4 ** n) * 2
        r -= length
    
    else: # 4 사분면
        answer += (4 ** n) * 3
        r -= length
        c -= length

print(answer)

'''
N = 1, 출발지점 : 0
N = 2, 출발지점 : 0, 4(4^1), 8, 12 (각 사분면 길이 2^1)
N = 3, 출발지점 : 0, 16(4^2), 32, 48 (각 사분면 길이 2^2)
N = 4, 출발지점 : 0, 64(4^3), 128, 192 (각 사분면 길이 2^3)
'''