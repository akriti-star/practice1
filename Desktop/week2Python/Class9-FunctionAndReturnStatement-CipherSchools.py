def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock", name)
sheldon_knock("leonard")

def sheldon_knock (me,times=3):
    for _ in range(times):
        print("knock knock knock",me)
sheldon_knock("penny",100)

#Return Statement
def add (a,b):
    return a+b
a= add (1,3)
print(a)
