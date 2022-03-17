n, m = map(int, input().split())

dict = {input(): 1 for _ in range(n)}
people_list = []


for i in range(m):
    people = input()
    if people in dict.keys():
        people_list.append(people)
print(len(people_list))
print('\n'.join(sorted(people_list)))
