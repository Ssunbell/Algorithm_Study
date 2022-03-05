text = input()
change = text.replace('dz=','_').replace('lj','_').replace('nj','_')
diff = list(change).count('_')
remainder = change.replace('=','').replace('-','').replace('_','')
print(diff + len(remainder))

#####################

s = input()
len_s = len(s)
str_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

ans = 0
for i in str_list:
    ans += str(s).count(i)
print(len_s - ans)