n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))

negative = (b for b in books if b < 0)
positive = (b for b in books[::-1] if b > 0)
distance = 0
print(books)
def gen():
    yield 0

if books[0] >= 0:
    positive = gen()
if books[-1] <= 0:
    negative = gen()

neg_max = abs(next(negative))
pos_max = next(positive)

if pos_max >= neg_max:
    distance += pos_max + (neg_max * 2)
else:
    distance += (pos_max * 2) + neg_max
    
## positive
p = 0
for pos in positive:
    p += 1
    if p % m == 0:
        distance += pos * 2

## negative
n = 0
for neg in negative:
    n += 1
    if n % m == 0:
        distance -= neg * 2
        
print(distance)