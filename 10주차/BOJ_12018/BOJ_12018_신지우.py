n,m=map(int,input().split()) 
result=[]

for k in range(n):
  p,l=map(int,input().split()) 
  mileage=list(map(int,input().split())) 
  mileage.sort(reverse=True) 

  if p<l: 
    result.append(1) 
  else:
    result.append(mileage[l-1]) 
result.sort() 

cnt=0
for i in result: 
  m-=i 
  cnt+=1 
  if m<0: 
    print(cnt-1) 
    break

if m>0: 
  print(cnt)