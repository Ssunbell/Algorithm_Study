a, b = input().split()

for i, char in enumerate(a):
    b_index = b.find(char)
    if b_index != -1:
        a_index = i
        break

for i, char in enumerate(b):
    if i == b_index:
        print(a)
    else:
				# .을 먼저 찍고 + b 문자 한개 + 다시 남은 만큼 . 찍기
        print("." * a_index + char + "." * (len(a) - a_index - 1))