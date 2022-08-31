def solution(priorities, location):
    max_v = max(priorities)
    cnt = 0
    
    while priorities:
        if priorities[0] < max_v:
            priorities.append(priorities.pop(0))
        else:
            if location == 0:
                cnt += 1
                break
            priorities.pop(0)
            cnt += 1
            max_v = max(priorities)

        location = (location - 1) % len(priorities)

    return cnt