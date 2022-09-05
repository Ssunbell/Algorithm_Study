n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

distance = sorted([sensor[i] - sensor[i-1] for i in range(1, n)], reverse=True)
print(sum(distance[k-1:]))
'''
[3, 6, 7, 8, 10, 12, 14, 15, 18, 20]
   3  1  1  2   2   2   1   3   2
=> [3, 3, 2, 2, 2, 2, 1, 1, 1]
값이 큰 위치에 칸막이를 넣는다는 느낌. 칸막이는 집중국의 경계선을 의미
k개의 칸막이를 넣을 경우 (k+1)개의 영역이 생기므로
k-1개의 칸막이 생성
칸막이의 위치는 고려할 필요가 없음. 문제의 목표는 수신 가능 영역의 길이를 구하는 것이므로
위치는 알아서 정해진다고 가정(경우의 수를 구하는 것이 아닌 경우의 수 갯수를 구함)
'''