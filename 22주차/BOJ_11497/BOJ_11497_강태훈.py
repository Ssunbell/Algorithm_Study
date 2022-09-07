import sys
input = sys.stdin.readline
testCase = int(input())
for _ in range(testCase):
    N = int(input())
    L = sorted(map(int, input().split()))
    answer = L[-1] - L[-2]
    for i in range(2, N):
        answer = max(answer, L[i] - L[i-2])
    print(answer)

'''
길이정렬 후 최댓값을 기준으로 두개씩 뽑아내어 큰 값 부분, 작은 값 부분을 각각 반대편에 붙히면 되는 그리디 문제로 해석함

길이 순 정렬 후 최댓값을 뽑아내어 기준점으로 사용
나머지의 홀수 인덱스는 우측, 짝수 인덱스는 좌측에 붙힘
이후 양 옆과의 차이가 최대가 되는 값을 찾고 출력함

아이디어는 이러하지만, 굳이 배열을 수정하는 과정은 필요없어보여 i, i - 2 인덱스를 비교하는 방식으로 변경
answer의 초기값을 최댓값 두개의 차로 설정하여 위 과정으로 고려되지 않는 경우를 추가함.
'''
