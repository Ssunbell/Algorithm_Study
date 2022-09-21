n = int(input())

for i in range(n):
    if i % 2 == 0: # 짝수일때
        print("* " * n) 
    else:
        print(" *" * n)
