n = int(input())

element_locations = []

for i in range(n):
    x, y = map(int, input().split())
    element_locations.append((x, y))

element_locations.sort(key=lambda x: (x[0], x[1]))

for element_location in element_locations:
    print(element_location[0], element_location[1])