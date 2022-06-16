import sys

input = lambda: sys.stdin.readline().rstrip()

test_case = int(input())

answer = []

for i in range(test_case):
    n, m = map(int, input().split())
    doc_imp = list(map(int, input().split()))
    idx = list(range(len(doc_imp)))
    idx[m] = 'target'

    cnt = 0

    while True:

        if doc_imp[0] ==  max(doc_imp):
            cnt += 1

            if idx[0] == 'target':
                print(cnt)
                break
            else:
                doc_imp.pop(0)
                idx.pop(0)

        else:
            doc_imp.append(doc_imp.pop(0))
            idx.append(idx.pop(0))