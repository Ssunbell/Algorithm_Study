# 91%에서 틀림
import sys
from collections import deque

input_s = lambda : sys.stdin.readline().strip()
s = input_s()

st = deque()
st.append("*")
for i in s:
    if i == "(":
        st.append(i)
    elif i == "[":
        st.append(i)
    elif i == ")":
        if st[-1] == "(":
            st.pop()
            st.append(2)
        elif isinstance(st[-1],int):
            curr = 0
            while True:
                if isinstance(st[-1],int) == False:
                    break
                curr += st.pop()
            if st[-1] == "(":
                st.pop()
                st.append(curr*2)
            else:
                st.append(curr)
        else:
            st.append(i)
    elif i == "]":
        if st[-1] == "[":
            st.pop()
            st.append(3)
        elif isinstance(st[-1],int):
            curr = 0
            while True:
                if isinstance(st[-1],int) == False:
                    break
                curr += st.pop()
            if st[-1] == "[":
                st.pop()
                st.append(curr*3)
            else:
                st.append(curr)
        else:
            st.append(i)
st.popleft()
try:
    result = sum(st)
except:
    result = 0

print(result)
