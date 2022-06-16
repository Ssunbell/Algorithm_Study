import sys
input = sys.stdin.readline

test_cases = int(input())

for i in range(test_cases):
    n, m = map(int, input().split())
    doc_imp = list(map(int, input().split()))
    idx = [0] * len(doc_imp)
    idx[m] = "T"
    cnt = 0
    while True:
        if doc_imp[0] == max(doc_imp):
            cnt += 1
            if idx[0] == "T":
                print(cnt)
                break
            else:
                doc_imp.pop(0)
                idx.pop(0)
        else:
            doc_imp.append(doc_imp.pop(0))
            idx.append(idx.pop(0))
