N, M = map(int, input().split())

unheared = {input(): 0 for i in range(N)}

for i in range(M):
    name = input()
    if name not in unheared:
        unheared[name] = 0
    else:
        unheared[name] += 1

print(sum(unheared.values()))

result = []
for i in unheared:
    if unheared[i] == 1:
        result.append(i)

result = sorted(result)

for i in result:
    print(i)