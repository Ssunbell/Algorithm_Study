wood_pieces = list(map(int, input().split()))

for i in range(5):
    for j in range(4):
        if wood_pieces[j] > wood_pieces[j+1]:
            wood_pieces[j], wood_pieces[j+1] = wood_pieces[j+1], wood_pieces[j]
            print(*wood_pieces)

        if wood_pieces == [1,2,3,4,5]:
            break