def solution(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    cnt = [True]*(n+1)
    m = int(n**0.5)
    c = 0
    for i in range(2, m+1):
        if cnt[i]==True: # 만약 소수면 # i가 소수인 경우 
            for j in range(i+i, n+1, i):
                cnt[j] = False # 소수의 배수는 소수가 아님
    for i in range(2, n+1): # 소수 개수 카운트
        if cnt[i]:
            c+=1
    return c