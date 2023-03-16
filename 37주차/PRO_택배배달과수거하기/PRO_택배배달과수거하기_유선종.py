from heapq import heappush, heappop

def solution(cap, n, deliveries, pickups):
    hq_d = []
    hq_p = []
    for idx, d in enumerate(deliveries):
        if d: heappush(hq_d, (-(idx+1), d))
    for idx, p in enumerate(pickups):
        if p: heappush(hq_p, (-(idx+1), p))

    answer = 0
    while hq_d or hq_p:
        capability = cap
        dist = 0
        while hq_d and capability:
            house, box = heappop(hq_d)
            dist = max(dist, -house)
            capability -= box
            if capability < 0:
                heappush(hq_d, (house, -capability))
                capability = 0
        
        pick = cap
        while hq_p and pick:
            house, box = heappop(hq_p)
            dist = max(dist, -house)
            pick -= box
            if pick < 0:
                heappush(hq_p, (house, -pick))
                pick = 0

        answer += dist * 2
        
    return answer