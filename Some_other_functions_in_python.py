'''
closure function
partial function
composed function
callback function
recursive functions
'''
print("Closure Function")
def outer(sms):
    def inner():
        return str(sms)
    return inner
say_hi=outer("Hello")
print(say_hi())

print()
print("Partial Function")
from functools import partial
def gst(base_price,tax_price):
    return base_price*(1+tax_price)
price_cal=partial(gst,tax_price=0.18)
print(price_cal(1000))

print()
print("Composed Function")
def add(a,b):
    return a+b
def mul(a):
    return a*a
def process(a,b):
    return mul(add(a, b))
print(process(2,3))
print()
# Recursive function:
print("Recursive function ")
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))


