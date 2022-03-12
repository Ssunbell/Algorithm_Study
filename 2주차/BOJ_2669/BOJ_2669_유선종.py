space = [list(map(int,'0'*100)) for _ in range(100)]

for _ in range(4):
    a, b, c, d = map(int, input().split())
    
    for depth_len in range(b, d):
        for base_len in range(a, c):
            space[depth_len][base_len] = 1

print(sum(sum(space, [])))
    