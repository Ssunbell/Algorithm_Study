import sys
sys.setrecursionlimit(10**6)


def find(parent, f):
    if get(parent, f) == f:
        return f
    parent[f] = find(parent, parent[f])
    return parent[f]


def union(parent, f1, f2):
    p1, p2 = find(parent, f1), find(parent, f2)
    parent[min(p1, p2)] = max(p1, p2)


def get(dictionary, val):
    if val not in dictionary:
        dictionary[val] = val
    return dictionary[val]


def solution(k, room_number):
    parent = {}
    booked = {}
    for i in room_number:
        loc = i
        if i in booked:
            loc = find(parent, i)
        booked[loc] = True
        union(parent, loc, loc+1)
    return list(booked.keys())
