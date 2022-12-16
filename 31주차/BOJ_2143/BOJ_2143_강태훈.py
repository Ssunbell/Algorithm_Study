import sys
from itertools import combinations, accumulate
from collections import Counter
input = sys.stdin.readline

partsum = lambda arr : Counter([b-a for a,b in combinations(accumulate([0]+arr),2)])
get_set = lambda T,a,b: sum([(aval*b[T-akey]) for akey, aval in a.items() if (T-akey in b)])

if __name__=="__main__":
    T,n = int(input()),int(input())
    a = partsum(list(map(int, input().split())))
    m = int(input())
    b = partsum(list(map(int, input().split())))
    print(get_set(T,a,b))