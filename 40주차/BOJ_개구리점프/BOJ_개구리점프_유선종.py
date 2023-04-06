import sys

class WeightedUF():
    def __init__(self, array_len):
        self.parent = [-1 for _ in range(array_len)]
        
    def find(self, x):
        if self.parent[x] < 0: # 루트 노드일 경우
            return x
        else:
            y = self.find(self.parent[x])
            self.parent[x] = y
            return y
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y : return
        
        if self.parent[x] < self.parent[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y

if __name__=='__main__':
    input = lambda: sys.stdin.readline().rstrip()
    N, Q = map(int, input().split())
    connected = sorted([tuple(list(map(int, input().split())) + [i]) for i in range(N)])
    uf = WeightedUF(N)
    now_start, now_end, _, now_idx = connected[0]
    for i in range(1, N):
        next_start, next_end, _, next_idx = connected[i]
        
        if now_start <= next_start <= now_end:
            uf.union(now_idx, next_idx)
            
            if next_end >= now_end:
                now_start, now_end, now_idx = next_start, next_end, next_idx
        else:
            now_start, now_end, now_idx = next_start, next_end, next_idx
    
    for _ in range(Q):
        s, e = map(int, input().split())
        if uf.find(s - 1) == uf.find(e - 1):
            print(1)
        else:
            print(0)