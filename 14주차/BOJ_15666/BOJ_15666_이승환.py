from collections import deque
import sys

input_s = lambda : sys.stdin.readline().strip()

n, m = map(int,input_s().split())
s = deque(map(int,input_s().split()))

sets = sorted(set(s))

for s in sets:
    root = s
    st = deque()
    st.append(s)

    pr = deque()
    while st:
        curr = st.pop()
        pr.append(curr)

        if len(pr) == m:
            
            
        for i in sets:
            if i >= pr[-1]:
                st.append(i)




result = deque()



