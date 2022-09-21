croatia_alphabet = input()

croatia =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for i in croatia:
    if i in croatia_alphabet:
        croatia_alphabet = croatia_alphabet.replace(i, '.')
print(len(croatia_alphabet))