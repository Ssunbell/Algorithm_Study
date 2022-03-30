n, m = map(int, input().split())

lab = []
two_len = 0
one_len = 0
for i in range(n):
    temp = list(map(int, input().split()))
    two_len += temp.count(2)
    one_len += temp.count(1)
    lab.append(temp)
print(lab)
print(two_len)
print(one_len)

if one_len + 3 >= two_len:
    pass
else:
    pass

'''
아이디어

1. 1이 2보다 많거나 같다면 물을 막을 둑이 있으므로
물길을 막아 물이 넘치지 않도록 차단한다.
 - 먼저 1을 넣어서 둑을 쌓아본다.
 - 2의 갯수를 늘리면서 물이 어떤 물길을 따라 흐르는지 파악한다.
 - 이 과정을 반복하여 최대한 0을 살리는 방법을 채택한다.
 

2. 2가 1보다 더 많다는 것은 강이 범람하는 것을 막을 수 없으므로
내 한몸 살리기 위해 물을 막는 것이 아닌 건물 위로 올라간다.
 - 2의 갯수를 늘리면서 홍수가 일어나는 과정을 구현할 필요가 없다.
   어짜피 물에 잠긴다.
 - 따라서 가지고 있는 1을 이용하여 최대한의 공간을 확보한다.
'''