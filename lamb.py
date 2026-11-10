#Normal function:
def square(a):
     return a*a

#Lambda function:
square=lambda a:a*a
rectangle=lambda a,b:a*b
triangle=lambda a,b:0.5*a*b
print("Square:" ,square(5))
print("Rectangle:", rectangle(5,4))
print("Triangle:",triangle(6,4))