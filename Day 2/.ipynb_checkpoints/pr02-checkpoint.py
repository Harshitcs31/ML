# is used for commenting

print (4+5)#it gives addition
print(8/3)#It gives value in float
print(8//3)#floor division operator----  //
print("hello"*3)#gives string 3 times
print("Hello"+"Gaurav")#string with no space
#egs of string with space
print("hello "+"garvit")
print("hello"+" garvit")
print("hello"+" "+"garvit")
print(10%7)#modulo operator(%)gives remainder

a="python"
b=10
print(id(a))#it gives the location of a in memory
print(id(b))#it gives the location of b in memory

a="Machine Learning"#now a will have machine learning in it
print(a,b)

import keyword #imports all keywords
print(keyword.kwlist)#displays all keywords
print(len(keyword.kwlist))#displays total no of keywords

# in python we can use multiple quotes also i.e ('''     ''')
#triple quote is used when we are writing multiple lines

a,b,c=20,50,60 #we can assign in single line also
print(a,b,c)

x=y=z=100
print(x,y,z)

print(2<3 and 7>6) # true when both are true-------> logical and
print(2<3 or 7<6) # true when any one is true------> logical or

a=5
print(type(a))#gives data type
a=21+4j
print(type(a))
a=[10,4,5,2+7j,"jekkp"] # list
print(type(a))
a={10,4,5,2+7j,"jekkp"} # set
print(type(a))
a=(10,4,5,2+7j,"jekkp") # tuples
print(type(a))
b=10,4,5,2+7j,"jekkp" # tuples
print(type(b))
a={"name":"garvit","a":10,"complex":2+5j}
print(type(a))

c=2+3j
print(c.real,c.imag)
