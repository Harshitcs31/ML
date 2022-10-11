# a={"name":["garvit","gaurav","kalpit"],"age":[18,19,20]}
# print(type(a))
# print(a["name"])
# print(a["age"])
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
# a["phone_no"]=[342665436,6536546546,5654654]
# print(a)
# print(a["name"][0])
# print(a["name"][0][-1:-7:-1])
# a["name"][0]="harshita"
# print(a)


# a={'name':['garvit','gaurav'],'age':[19,20]}
# print(a)
# print(a.get('name'))
# c=20
# b='ML'
# print(c,b)
# print(c,b,sep='   ')
# print(c,end='#############')# print ke andar by default new line ke endl hota hai and seprator bhi hota hai
# print(b)# aab ye pehele c print karega then ######## then b ,agar end ko change nhi karte to line change hoti
# d=input('Enter your name')
# print('your name is',d)
# ##in below example num behaves as string
# num1=input('enter first number')
# num2=input('enter second number')
# print(num1+num2)

# #here we have typecasted num as int
# num1=int(input('enter first number'))
# num2=int(input('enter second number'))
# print(num1+num2)


# statements
# simple if
# age = int(input('Enter the age'))
# if age < 18:
#     print('gift')
# if age >= 18 and age <= 20:
#     print('Gift')
# if age > 20:
#     print('gbdxgf')

# ladder
# age = int(input('Enter the age'))
# if age < 18:
#     print('gift')
# elif age >= 18 and age <= 20:
#     print('Gift')
# else:
#     print('gbdxgf')

# nested
# age=int(input('Enter the age'))
# fav_no=int(input("Enter you favourite number(1-10)"))
# if age<18:
#    if fav_no<5:
#        print('garvit')
#    else:
#        print('gaurav')
# if age>=18 and age<=20 :
#    print('Gift')
# if age>20:
#   print('gbdxgf')

# program to find the greatest of three number
a, b, c = (int(input('Enter 1st number'))), (int(
    input('Enter 2nd number'))), (int(input('Enter 3rd number')))
# b = (int(input('Enter 2nd number')))
# c = (int(input('Enter 3rd number')))
d = [a, b, c]
d.sort()
print(d[2])
