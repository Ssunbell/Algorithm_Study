croatia_alpahbet = ["c=","c-","dz=","d-",'lj','nj','s=','z=']

word = input()

for i in croatia_alpahbet:
    word = word.replace(i,",")
print(len(word))