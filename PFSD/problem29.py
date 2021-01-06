n=int(input()) 
factors=[1] 
for i in range(2,n):
   if(n%i==0): 
      factors.append(i) 
factors.append(n) 
print(factors)
