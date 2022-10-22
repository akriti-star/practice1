x= int (input("enter the first number"))
y=int (input ("enter the second number"))
operator=input("enter your operator,[+,-,*,%,**,/,//]:")
if operator=="+":
    print (x+y)
elif operator=="-":
    print(x-y)
elif operator=="*":
    print(x*y)
elif operator=="%":
    print(x%y)
elif operator=="**":
    print(x**y)
elif operator=="/":
    print(x/y)
elif operator=="//":
    print(x//y)
else:
    print("invalid")