from typing import *
from collections import deque, defaultdict

def solution(n:int, lighthouse:List[List[int]]) -> int:
    answer = set()
    
    tree = defaultdict(list)
    for a, b in lighthouse:
        tree[a].append(b)
        tree[b].append(a)
    
    q = deque([])
    k = 1
    while not q:
        for i, node in tree.items():
            if len(node) == k:
                q.append(i)
        k += 1
    
    while q:
        light_on = []
        for node in q:
            for root in tree[node]:
                if root not in answer:
                    answer.add(root)
                    light_on.append(root)
                tree[node].remove(root)
                tree[root].remove(node)
        
        for lighted_node in light_on:
            for node in tree[lighted_node]:
                tree[node].remove(lighted_node)
            tree[lighted_node] = []
            
        q = deque([])
        k = 1
        while not q:
            if not any(tree.values()): # 더이상 연결된 노드가 없는 경우
                break
                
            for i, node in tree.items():
                if len(node) == k:
                    q.append(i)
            k += 1

    return len(answer)