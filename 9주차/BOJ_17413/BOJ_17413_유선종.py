text = input()

tags = []
while True:
    try:
        start = text.index('<')
        end = text.index('>')
        tag = text[start:end + 1]
        tags.append(tag)
        text = text.replace(tag, "+", 1)
    except:
        break

storage = []
temp = ''
for i, t in enumerate(text):
    if t == '+':
        storage.append(temp)
        if temp != '':
            storage.append('')
        temp = ''
        
    elif t == ' ':
        storage.append(temp)
        storage.append(t)
        temp = ''
    else:
        temp = t + temp
        if i == len(text) - 1:
            storage.append(temp)

for i, txt in enumerate(storage):
    if txt == '':
        try:
            tag = tags.pop(0)
            storage[i] = tag
        except:
            break
        
print(''.join(storage))
