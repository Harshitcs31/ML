#multiline string
c='''rhhuiggtkl
hhthyguuh
grtiubji'''
print(c)

#Concept of indexing

a='Hello World'
print(a)

#positive indexing
print(a[0])#Gives First element i.e 'H'
print(a[6])#Gives 7th element i.e. 'W'
print(a[10])#gives 'd'

#negative indexing
print (a[-1])#Gives First element from end i.e 'd'

#concept of slicing
print(a[0:2])
print(a[-11:-9])
print(a[-7:-9:-1])

print(a[:2])
print(a[:10:2])

print(a[6:])
print(a[-5:])

#reversing a string through indexing
print(a[-1:-12:-1])
print(a[::-1])

print(a[-8:-6])

#string inbuilt functions
a='hello world'
print(a.capitalize())#makes h capital
print(a.title())#makes both h and w capital
print(a.center(50))#hello world will come centre
print(a.center(50,'#'))
print(a.count('l'))#count how many times l is there in the string
a=a.center(50)#now string has changes permanently
print(a)
print(a.lstrip())
print(a.rstrip())
print(a.strip())

a=a.strip()
print(a)
print(a.isupper())
print(a.islower())

a=a.upper()
print(a)

a=a.lower()
print(a)

print(len(a))

print(a.endswith('d'))
#below two operations give error this shows that string is immutable
#a[0]='m'
#del a[o]

b='gauravgupta2.cse25@jecrc.ac.in'
print(b.split('@'))
b=b.split('@')

print ('@'.join(b))

#######################################################################

#list
m=[12,'hi',2.3,500]
print(m[0])
print(m[1:3])

print('hi' in m)
print('hello' in m)
print('hi' not in m)

print(2*m)#repetetion of list
m+=['new val']#add of new value in list
print(m)

#m=m.append('abc')#alternate way of adding elements
print(m)
m=m.insert(2,'hello')
print(m)
mp=m.pop()
print(mp)

m.pop(0)
print(m)

print(m.clear())

n=[12,45,52,100]
print(n.reverse())
print(n.sort())
print(max(n))
print(min(n))
print (n.index(45))

print(m[1][0])
###################################################################

#Tuple
t=52,23,'abc'
print(type(t))
print(len(t))
print(t.index('abc'))
print(t[0])
#below two operations will give error this shows that tuple is immutable
t[0]=42
del t[1]
#slicing in tuple
print(t[:2])

#################################################################

#Set
s={1,1,2,2,3,4,4,3}
print(type(s))
print(s)
#below two operations are not possible in set
print(s[0])
print(s[0:2])

s2={23,3,4,41}
print(s.intersection(s2))
print(s.union(s2))
print(s.add(100))
print(s.discard(100))
print(s.remove(3))
