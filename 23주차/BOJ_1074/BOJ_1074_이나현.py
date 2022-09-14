#[Z]
def func(i0, j0, length):
    global r, c, count
    if length == 1:
        return
    length //= 2
    if r < i0 + length:
        if c < j0 + length: # 1구간(왼쪽 위)
            func(i0, j0, length)
        else:               # 2구간(오른쪽 위)
            count += length**2
            func(i0, j0+length, length)
    else:
        if c < j0 + length: # 3구간(왼쪽 아래)
            count += (length**2) * 2
            func(i0+length, j0, length)
        else:               # 4구간(오른쪽 아래)
            count += (length**2) * 3
            func(i0+length, j0+length, length)
    

N, r, c = map(int, input().split())
count = 0
func(0,0,2**N)
print(count)