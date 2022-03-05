text = input()

if text == text[::-1]: print(1)
else: print(0)

##########################

text = input()
text_reverse = ''

for i in range(1 + len(text)):
    text_reverse += text[-i]
if text == text_reverse: print(1)
else: print(0)