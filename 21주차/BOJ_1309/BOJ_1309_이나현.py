#[동물원]
N = int(input())
arr = [[0,0,0] for _ in range(N)]
arr[0] = [1,1,1]
for i in range(1, N):
    arr[i][0] = (sum(arr[i-1]))%9901
    arr[i][1] = (arr[i-1][0] + arr[i-1][2])%9901
    arr[i][2] = (arr[i-1][0] + arr[i-1][1])%9901
print(sum(arr[N-1])%9901)

# 참고 - 나머지 분배법칙
# (A+B)%p = [(A%p) + (B%p)] % p
# (AxB)%p = [(A%p) * (B%p)] % p
# (A-B)%p = [(A%p) - (B%p)+p] % p