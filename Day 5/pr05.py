 
d1={'name':['akash','akshat','sunny'],'semester':[2,1,2]}
print(d1)
d1['name']+=['bunny']#adding a new value to existing key
print(d1)
d1['name']+='bunny'
print(d1)

d1['name'].insert(1,'gaurav')#adding a new value to a specific position in a existing key
print(d1)

d1['sem']=d1.pop('semester')#changing name of a key
print(d1)

#f-string/string format
a='Akshat'
b='Upflairs'
print(f'Hi {a} welcome to {b}')
print('hi {} welcome to {}'.format('Akshat','Upflairs'))
print('hi {} welcome to {}'.format(a,b))

#------------------------------------------------------------------------

#Loops
for i in[1,2,3,4,5]:
     print(i)

for i in['a','b','c','d']:
     print(i)

for i in 'HelloWorld':
     print(i)

for i in "HelloWorld":
     print('HelloWorld')

for x in "HelloWorld":
     print(x) #x and i in all these loops are local variables

for x in "HelloWorld":
     print(x,end=' ')
     print('Hello')
print('helloworld')#it is out of the loop

for i in range(6):
    print(i)

# Alt+3 is used to cooment all selected lines

#Ques=make another list from given list and add 1 to every element
t=[12,15,18,20]
#for i in t:
#    c=[print (i+1)]
m=[]
for i in t:
    m.append(i+1)
print(m)

#Ques2 Print even and Greater than 10 from given list
t=[12,15,18,20,8,10,16]
print(t)
m=[]
for i in t:
    if i>10 and i%2==0:
        m.append(i)
print(m)

#home task:-make twice of first four nos
t=[2,5,8,6,8,10,16]
for i in t:
    if i<4:
     print(i*2)
    else:
     print(i)
#-------------------------------------------------------------------
#while loop
num=1
while num<=5:
    print('hello')
    num+=1

#Infinite loop
#while True:
#    print('This is infinite loop')

num=10
while num>0:
   print(num)
   num-=1

#continue example
for i in [1,2,'abc','xyz',23,20]:
    if i=='xyz':
        continue
    print(i)

#break example
for i in [1,2,'abc','xyz',23,20]:
    if i=='xyz':
        break
    print(i)

#pass is used when we have to do nothing
for i in [1,2,'abc','xyz',23,20]:
    pass
