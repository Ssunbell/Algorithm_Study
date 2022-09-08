#[통나무 건너뛰기]
T = int(input())
for t in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    arr1 = arr[::2]
    arr2 = arr[1::2]
    arr2 = arr2[::-1]
    arr = arr1 + arr2
    answer = 0
    for i in range(N):
        answer = max(answer, abs(arr[i] - arr[i-1]))
    print(answer)