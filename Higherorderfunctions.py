print("Example for taking a fun as its input and returning fun as its output")
def new_fun(name):
    print(name)
def ano_fun(name,new_fun):
    return new_fun(name)
ano_fun("subha",new_fun)

# pure and impure functions:
print()
print("ImPure functions")
total=0
def add(amt):
    global total
    total+=amt
    print(total)
add(5)

print()
print("Pure Function")
def mul(r):
    return r*r
print(mul(5))
print()
print("Lambda function")
add=lambda a,b:a+b
print(add(2,3))

print()
print("Map")
l1=[1,2,3]
print(list(map(str,l1)))

print()
print("Filter")
l2=[1,2,3,4,5,6]
evens=list(filter(lambda x:x%2==0,l2))
print(evens)

print()
from functools import reduce
print("Reduce")

l3=[1,2,3,4,5]
res=reduce(lambda x,y:x+y,l3)

res1=reduce(lambda x,y:x if x>y else y,l3)

print(res)
print(res1)
