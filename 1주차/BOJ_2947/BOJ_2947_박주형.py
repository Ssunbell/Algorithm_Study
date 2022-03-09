tree_pieces = list(map(int, input().split()))

for i in range(len(tree_pieces)):
    for i in range(len(tree_pieces)-1):
        while tree_pieces[i] > tree_pieces[i+1]:
            tree_pieces[i], tree_pieces[i +
                                        1] = tree_pieces[i + 1], tree_pieces[i]
            print(*tree_pieces)
        if tree_pieces == [1, 2, 3, 4, 5]:
            break
