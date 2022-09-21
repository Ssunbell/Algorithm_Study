n = int(input()) # 3의 거듭제곱 

def get_stars(n):
    temp = []
    for i in range(len(n) * 3):
        if i // len(n) == 1:
            temp.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            temp.append(n[i % len(n)] * 3)
    return temp

star = ["***", "* *", "***"]
count = 0

while n != 3:
    n //= 3
    count += 1

for _ in range(count):
    star = get_stars(star)
    print(star)

for j in star:
   print(j)