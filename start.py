start=int(input("enter start:"))
end=int(input("enter end:"))
for n in range(start,end+1):
  if n>=1000 and n<=9999:
       a=n//1000
       b=n//100%10
       c=n//10%10
       d=n%10
       if a%2==0 and b%2==0 c%2==0 and d%2==0:
         for i in range(1,100):
           if i*i==n:
             print(n)

