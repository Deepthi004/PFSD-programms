
n = int(input("Please enter the number: "))
if n > 1:
   for i in range(2,n//2):
      if (n % i) == 0:
         print(n,"is not a prime number")
         print(i,"times",n//i,"is",n)
         break
      else:
         print(n,"is a prime number")
else:
   print(n,"is not a prime number")
