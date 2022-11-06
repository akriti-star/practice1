def name(x):
    return lambda a,b,c:(a+b+x)*c
num=name(2)
print(num(5,7,5))