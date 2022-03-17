n, m = map(int, input().split())
poketmon_dict = {}

for i in range(n):
    poketmon_name = input()
    poketmon_dict[poketmon_name] = str(i+1)
    poketmon_dict[str(i+1)] = poketmon_name

phd_test = [input() for j in range(m)]
answer = []

for test in phd_test:
    answer.append(poketmon_dict[test])

print(*answer, sep='\n')
