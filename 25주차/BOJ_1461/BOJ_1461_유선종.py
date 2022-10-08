## 제너레이터 사용 안한 코드 
n, m = map(int, input().split())
books = list(map(int, input().split()))

negative = sorted([b for b in books if b < 0])
positive = sorted([b for b in books if b > 0], reverse=True)
distance = 0

if not positive:
    positive = [0]
elif not negative:
    negative = [0]

if abs(min(negative)) >= max(positive):
    distance +=  negative[0]
else:
    distance -= positive[0]
    
## positive
for i in range(0, len(positive), m):
    distance += positive[i] * 2

## negative
for i in range(0, len(negative), m):
    distance -= negative[i] * 2

print(distance)

## 제너레이터를 사용해도 메모리와 시간이 동일한 코드
'''
n, m = map(int, input().split())
books = sorted(list(map(int, input().split())))
pos = []
neg = []

# books가 정렬되어 있으므로 알아서 정렬되어 있음
for b in books:
    if b > 0:
        pos.append(b)
    elif b < 0:
        neg.append(b)

def gen():
    yield 0

if not neg:
    negative = gen()
else:
    negative = (b for b in neg)

if not pos:
    positive = gen()
else:
    positive = (b for b in pos[::-1])
    
distance = 0

# positive와 negative의 첫번째 iter값을 꺼냄
neg_max = abs(next(negative))
pos_max = next(positive)

if pos_max >= neg_max:
    distance += pos_max + (neg_max * 2)
else:
    distance += (pos_max * 2) + neg_max
    
# positive와 negative의 두번째 iter값부터 for loop
p = 0
for pos in positive:
    p += 1
    if p % m == 0:
        distance += pos * 2

n = 0
for neg in negative:
    n += 1
    if n % m == 0:
        distance -= neg * 2
        
print(distance)
'''

## 제너레이터를 사용했음에도 시간이 늘어난 코드1
'''
n, m = map(int, input().split())
books = sorted(list(map(int, input().split())) + [0])
zero_index = books.index(0)
pos = books[zero_index+1:][::-1][::m]
neg = books[:zero_index][::m]

def gen():
    yield 0

if not neg:
    negative = gen()
else:
    negative = (b for b in neg)

if not pos:
    positive = gen()
else:
    positive = (b for b in pos)
    
distance = 0

# positive와 negative의 첫번째 iter값을 꺼냄
neg_max = abs(next(negative))
pos_max = next(positive)

if pos_max >= neg_max:
    distance += pos_max + (neg_max * 2)
else:
    distance += (pos_max * 2) + neg_max
    
# positive와 negative의 두번째 iter값부터 for loop
for pos in positive:
    distance += pos * 2

for neg in negative:
    distance -= neg * 2
        
print(distance)
'''

## 제너레이터를 사용했음에도 시간이 늘어난 코드2
'''
n, m = map(int, input().split())
books = sorted(list(map(int, input().split())) + [0])
zero_index = books.index(0)
pos = books[zero_index+1:][::-1]
neg = books[:zero_index]

if not neg:
    neg = [0]
    neg_indices = []
else:
    neg_indices = (idx for idx in range(0, len(neg), m))

if not pos:
    pos = [0]
    pos_indices = []
else:
    pos_indices = (idx for idx in range(0, len(pos), m))
    
distance = 0

# positive와 negative의 첫번째 iter값을 꺼냄

if (-1) * neg[0] > pos[0]:
    distance += neg[0]
else:
    distance -= pos[0] 
    
# positive와 negative의 두번째 iter값부터 for loop
for idx in pos_indices:
    distance += pos[idx] * 2
    
for idx in neg_indices:
    distance -= neg[idx] * 2
        
print(distance)
'''

# 제너레이터를 사용했음에도 시간이 늘어난 코드3
'''
n, m = map(int, input().split())
books = sorted(list(map(int, input().split())) + [0])
zero_index = books.index(0)
pos = books[zero_index+1:][::-1]
neg = books[:zero_index]

def gen():
    yield 0

if not neg:
    negative = gen()
else:
    negative = (b for b in neg[::m])

if not pos:
    positive = gen()
else:
    positive = (b for b in pos[::m])
    
distance = 0

# positive와 negative의 첫번째 iter값을 꺼냄
neg_max = abs(next(negative))
pos_max = next(positive)

if pos_max >= neg_max:
    distance += pos_max + (neg_max * 2)
else:
    distance += (pos_max * 2) + neg_max
    
# positive와 negative의 두번째 iter값부터 for loop
for pos in positive:
    distance += pos * 2

for neg in negative:
    distance -= neg * 2
        
print(distance)
'''