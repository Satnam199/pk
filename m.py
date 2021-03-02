# a=int(input('enter a number:'))
# flag=0
# for i in range(2,a):
#     for j in range(i):
#         if a%i==0:
#             flag=1
# if flag==0:
#     print('it is a prime number') 
# else:
#     print('not prime number')               

# n=int(input('enter a number:'))
# a=0
# b=1
# sum=0
# while n>sum:
#     print(sum)
#     a=b
#     b=sum
#     sum=a+b


# a=5
# for i in range(a):
#     for j in range(a-i):
#         print(end= ' ')
#     for k in range(i+1):
#         print('8',end= '')

#     print()    


# recursion

# def fac(x):
#     if x==1:
#         return 1
#     else:
#         return x*fac(x-1)

# n=5
# print(fac(n))

# a={'x':1,'b':'sat','c':5}
# print(a)


# x=2
# a=[{i:i*i for i in range(0,5,2)}]
# print(a)


# dict1={'n':'sat','a':23,'roll':4  }
# x=[(i,dict1[i]) for i in dict1]
# print(x)
# for i in range(len(dict1)):
#     print(i,dict1[i])




# a,b=input('enter the name and age:').split()
# print(a,b)


# name='satnam'
# age=43
# print(f'hello {name} your age is {age}')


# a=int(input('enter a number of a:'))
# b=int(input('enter a number of b:'))
# c=int(input('enter a number of c:'))
# a,b,c=input('enter a number ').split()
# x=int(a)+int(b)+int(c)
# print(f'average {x}')

# a='1 2 '
# b='....'
# print(a.replace(''))

# a='he is good and he is well'
# print(a.replace('and','5',1))


# a='my name is satnam singh'
# print(a.find('name'))


# numbergame={}
# numbergame[(1,2,4)]=8
# numbergame[(4,2,)]


# x={'a':2,'b':6,'c':7}
# # for key,value in x.items():
# #     print(key,value)
# for i in enumerate(x.items()):
#     print(i)

# a={0:0,1:1,2:2}
# # a.popitem()
# a.clear()
# print(a)


# import random
# print(random.randrange(10,100,3))

# import random
# a=[2,5,76,56,89]
# print(random.sample(a,3))

# a=[1,5,7,8]
# print(type(a))
# print(a)


# from array import *
# a=array('f',[1.0,5.9,7.8,9.8])
# # print(a[0])
# a.insert(0,980.0)
# print(a)
 
# from numpy import*



# a={'s':1,'b':2,'c':78}
# for i in enumerate (a.items()):
#     print(i)
# a.popitem()
# print(a)


# a='hey,my name is sat,i am'
# a=a.split(',')
# print(a)

# a='____sat   '
# a=a.lstrip('_')
# print(a)
# import random
# lowerletter='abcdefghijklmnopqrstuvwxyz'
# upperletter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number1='0123456789'
# special='#@$'
# concate=lowerletter + upperletter + number1 + special
# print(concate)
# f=''.join(concate)
# print(f)



# y=''.join(concate)
# print(y)
# d=random.sample(concate,8)
# z=''.join(d)
# print(z)


# class Mobile:
#     def __init__(self,m):
#         self.model=m
#     def show_model(self,p):
#         price=p
#         print('Modle:', self.model,'price:',price)

# samung=Mobile('satnam')
# samung.show_model(1000)


# class satnam:
#     def show_model(self):
#         print('my name is satnam')
# samsung=satnam()
# samsung.show_model()
# print(id(samsung))
# print()


# realme=satnam()
# realme.show_model()
# print(id(realme))

# a=(1,2,'sat')
# print(type(a))
# a=list(a)
# print(a)


# print('sat' in a)

# a=True
# print(type(a))

# x=str(a)
# print(a)



# n=int(input('enter a number:'))
# a=0
# b=1
# sum=0
# while n>=sum:
#     print(sum,end=' ')
#     a=b
#     b=sum
#     sum=a+b


# a=int(input('enter a number:'))
# flag=0
# for i in range(2,a):
#     if a%i==0:
#         flag=1
# if flag==0:
#     print('prime number')
# else:
#     print('non prime number')               


# a=int(input('enter a number:'))
# rev=0
# x=a
# while a>0:
#     rev=(a%10)+rev*10
#     a=a//10
# print(rev)
# if rev==x:
#     print('it is pelindrom')
# else:
#     print('not palindrome')    



# a=5
# for i in range(a):
#     print((i+1)*"* ")


# a=5

# for i in range(1,a):
#     for j in range((a*2)-i+1):
#         print(end = ' ')
#     for k in range(1,i+1):
#         print("* ",end ='') 
#     print('\n')      


# def calculator(a,b,op):

#     if op=='+':
#         return(' sum is ',(a+b))
#     elif op=='-':
#         return('subtraction is',(a-b)) 
#     elif op=='*':
#         return('multiply is ',(a*b))
#     elif op=="/":
#         return('division is ',(a/b))
#     elif op=='**':
#         return('power is ',(a**b))    
# if __name__== '__main__':
#     x=int(input('enter a number a : '))
#     y=int(input('enter a number b : '))
#     z=input('enter a operation op : ')                   
#     print(calculator(x,y,z))  

# import pywhatkit as kit

# kit.sendwhatmsg('+919653077333','helo',19,3)

# kit.playonyt('python')


# a=int(input('enter a number a : '))
# b=int(input('enter of number b : '))
# if a>b:
#     print('a is maximum ')
# elif a==b:
#     print('a and b are equal')

# else:
#     print('b is maximum')

# a=int(input('enter a number :'))
# sum=0
# temp=a


# power=len(str(a))


# while a>0:
#     # var=temp%10
#     # print(sum)
#     sum=sum+(a%10)**power
    
    
#     a=a//10
    
# print(sum)


# if temp==sum:
#     print('it is armstron')
# else:
#     print('not armstrong')    
    
# from textblob import TextBlob

# # incorrect_words=['goodd','spellinngs','havee']
# incorrect=[input('enter a words:')]

# correct_words=[]

# for i in incorrect:
#     correct_words.append(TextBlob(i))
# for j in correct_words:
#     print(j.correct())    
  


# class Class():
#     student=10
#     teacher=1
#     def tech(self):
#         print('python')
# object1=Class()
# print(object1.student)
# object2=Class()

# print(object2.teacher)


# class Institute:
#     def __init__(self,students,subject):
#         self.a=students
#         self.b=subject

#     def tech(self):
#         print(f'this institute have {self.a} student and it teaches {self.b}')

#     def tech(self):
#         print('python')    
        
# x=Institute(10,'data structure')
# # print(x.a)    
# print(x.tech())



# class laptop():
#     def __init__(self,weight,color,ram):
#         self.a=weight
#         self.b=color
#         self.c=ram
#     def typing_speed(self,speed):
#         print(f'keyboard speed is {speed}')

# o1=laptop(5,'red',8)
# print(o1.b)
# print(o1.typing_speed(35))


# class Car():
#     def __init__(self,color,weight,seats):
#         self.a=color 
#         self.b=weight
#         self.c=seats
#     def average(self,average):
#         print(f'average of car is {14}')

# o1=Car('brown',70,8)
# print(o1.c)


# class student:

#     def __init__(self,name,roll):
#         self.a=name
#         self.b=roll
#         self.c='dotalgo'
#     def update(self):
#         self.a='abc'

# a1=student('satnam',12)
# print(a1.c)
# a1.update()
# print(a1.a)
   
   
   
   
    # def marks(abc,marks):
    #     print('the marks of' + abc.a + 'is' +str(marks))

# o1=student('sat',12)
# o1.marks(70)


class student():
    def __init__(self,name,roll):
        self.a=name
        self.b=roll
    def marks(self,marks):
        print(self.a + str(marks))

# class coder(student):
#     pass

class coder(student):
    def __init__(self,name,roll,coder_id):
        student.__init__(self,name,roll)
        self.coder_id=coder_id

s1=coder('abc',101,'sa101')
print(s1.coder_id) 
s1.marks(80)

# o1=coder('abc',101)
# print(o1.b)
# o1.marks(100)







