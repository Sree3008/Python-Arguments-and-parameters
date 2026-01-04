#Default Arguments
def add(x=5):
    return x
print(add())


# Positional Arguments
def sub(y,x):
    return y-x
print(sub(2,3))


# Keyword Arguments
def mul(s,y):
    return s*y
print(mul(y=3,s=2))

# Variable Length Arguments
def multi(*args):
    return sum(args)
print(multi(1,2,3,4))

# Keyword Variable length Arguments
def kvar(**x):
    for i,v in x.items():
        print(f"{i}:{v}")
    
print(kvar(name='Subha',age=20))


# Keyword only arguments
def func(a,*,b):
    return a,b
print(func(1,b=2))


# Positional Only arguments
def pos(a,b,/,c):
    return a+b+c
print(pos(1,2,c=3))


# other example
def posi(x:int):
    return x
print(posi(2))

# Example with mixed Arguments
def newex(x,*args,**kwargs):
    print(x)
    print(args)
    print(list(map(str,kwargs.values())))
newex(1,2,3,4,5,name="subha")