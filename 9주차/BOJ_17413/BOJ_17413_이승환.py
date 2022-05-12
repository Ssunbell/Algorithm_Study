from collections import deque

s = input()

stack_s = deque()
queue_s = deque()
check = deque()
tag_on = False

for l in s:
    if l == "<":
        if queue_s or stack_s:
            for l_t in check:
                if l_t == "t":
                    print(queue_s.popleft(),end="")
                else:
                    print(stack_s.pop(),end="")
            check.clear()
        tag = ""
        tag += l
        tag_on = True
    elif l == ">" and tag_on:
        tag += l
        queue_s.append(tag)
        check.append("t")
        tag_on = False
    elif tag_on:
        tag += l
    elif l != " ":
        stack_s.append(l)
        check.append("l")
    else:
        for l_t in check:
            if l_t == "t":
                print(queue_s.popleft(),end="")
            else:
                print(stack_s.pop(),end="")
        print(" ",end="")
        check.clear()

for l_t in check:
    if l_t == "t":
        print(queue_s.popleft(),end="")
    else:
        print(stack_s.pop(),end="")
