a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))

while b:
     a,b=b,a%b
print("GCD=",a)