from bisect import bisect_left

treelen = [2**i-1 for i in range(1,51)]

def make_bin(number):
    binval = format(number, "b")
    bintreelen = treelen[bisect_left(treelen, len(binval))]
    return binval.zfill(bintreelen)

def check(s, e, binstr):
    if s == e:
        return binstr[s]
    m = (s + e) // 2

    l = check(s, m-1, binstr)
    if not l or (binstr[m] == "0" and l == "1"):
        return False

    r = check(m+1, e, binstr)
    if not r or (binstr[m] == "0" and r == "1"):
        return False

    if l == "0" and r == "0" and binstr[m] == "0":
        return "0"
    return "1"

def solution(numbers):
    bins = map(make_bin, numbers)
    return [int(check(0, len(binnum)-1, binnum)) for binnum in bins]