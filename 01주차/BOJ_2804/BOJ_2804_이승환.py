A, B = map(str,input().split())

for a in A:
    if a in B:
        word = a
        break

anum = A.index(word)
bnum = B.index(word)

ans = ""

for b in range(len(B)):
    if b == bnum:
        for a in A:
            ans += a
    else:
        for a in range(len(A)):
            if a == anum:
                ans += B[b]
            else:
                ans += "."
    ans += "\n"

print(ans)