if __name__ == '__main__':
    n, k = map(int, input().split())
    num = input()
    stk, cnt = list(), k
    for i in range(n):
        while(cnt > 0 and stk and stk[-1] < num[i]):
            stk.pop()
            cnt -= 1
        stk.append(num[i])
    print(''.join(stk[:n - k]))

"""
n자리수 숫자에서 k개를 지우면 무조건 n-k자리 나옴
앞에서부터 작은 수를 지워주는게 최선임
1924 -> 924 -> 94
1231234 -> 231234 -> 31234 -> 3234
4177252841 -> 477252841 -> 77252841 -> 7725284 or 7752841 or 7725841 -> 775841
            3           2           1                               0
"""