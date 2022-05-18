s = input()

spilt_minus = s.split("-")

number = []

for a in spilt_minus:
    split_plus = map(int,a.split("+"))
    number.append(sum(split_plus))

min_num = number[0]
for i in range(1,len(number)):
    min_num -= number[i]

print(min_num)