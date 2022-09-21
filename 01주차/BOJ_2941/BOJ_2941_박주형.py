croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()
for croatian_alphabet in croatian_alphabets:
    words = words.replace(croatian_alphabet, '.')
print(len(words))
