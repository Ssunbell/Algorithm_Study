n = int(input())

drinks = list(map(int, input().split())) 
drinks.sort(reverse=True) 

drink = drinks[0]

for i in drinks[1:]:
    half = i / 2 
    drink += half 
print('%g'%drink) #


