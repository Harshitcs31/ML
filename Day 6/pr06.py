# functions----------------------------------------------------------->
a=print('Hi how r u?')
print(a) # esa nhi kar sakte

#no i/p no o/p
def myfun():     #def keyword is used before a function
    print('This is a first function')

myfun() #function called
a=myfun() # none output aayega because ye koi output nhi de rha as ham isse store nhi kar sakte..

#no i/p but o/p
def second():
    return 'abc'

print(second()) # ye value return kar rha hai isliye print lagana padega
b=second()
print(b)  # output aayega because ye return kr rha h ham isse store kar sakte h..

#i/p but no o/p
def third(x):
    print('Hello '*x)# we can't store this hello
third(4)

#i/p and o/p both
def fourth(x):
    return x*10
a=fourth('Hello ')
print(a)

def fourth(x):
    print("hello")
    print("gaurav")
    print("garvit")
    return x*10
print(fourth(4))

def fourth(x):
    print('hi')
    return x**3 #return k baad vali values function call m nhi aati
    print('hello')
    print('djkgfb')

print(fourth(4))

def five(x,y,z):
    return x+y+z
print(five(3,4,5))

# multiple i/p and o/p
def six(x,y,z):
    return x+y+z
    
print(six(x=5,y=4,z=2))
print(six(y=5, x=4,z=2))
#print(six(4,3))

def seven(x,y,z=1):
    return x+y+z
print(seven(3,4))
print(seven(5,4,2))

#def seven(x=1,y,z=1):
    #return x+y+z # default argument hamesha last se define karte hai

#*args (always return a tuple)   *kwargs(always return a dictionary value)
#*args
def eight(*x):
    return x
print(eight())
print(eight(2))
print(eight(2,3,4))

#*kwargs
def nine(**x):
    return x
print(nine())
print(nine(name=['Bipul','garvit'],email='bipul@gmail.com'))
print(nine(n1=0,n2=[11,10,20],n3=['ab','xy']))

def Happy_birthday(x):
    print("Happy birthday to {x}"*4)
print(Happy_birthday('Gaurav'))
print(Happy_birthday('Garvit'))
    
def myfun(x,y,z):
    return x+y+z
print(myfun(2,4,6))

myadd=lambda x,y,z:x+y+z
print(myadd(5,9,7))

import math 
print(math.pi)
print(math.sqrt(81))
print(math.pow(2,3))
print(math.factorial(5))
import math as m
print(m.pi)
from math import sqrt as s
print(s(81))
import datetime as dt
print(dt.date.today())
import calendar
print(calendar.calendar(2022))
print(calendar.month(2022,9))
