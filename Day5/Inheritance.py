#inheritence:: aquiring all the attributes(variables) and behaviour(methods) from one class to another class is called inheritence.
# main purpose: the objective of inheritece are code reusability , avoid duplication.
# 4 tppes of inheritences are there
#1. single : we have only 1 parent class and 1 child class
#2. multi level inheritance:
#3.hirarcy inheritence: 1 parent have many child classes
#4.multiple inheritance: we have 1 child class will have multiple paresnt classes.


#Example1:simple inheritance
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
# class B(A):  # Now class B is a child of class A
#     def m2(self):
#         print("This is a m2 method from class B")

# bobject=B()
# bobject.m1()
# bobject.m2()


#Example2: simple inheritance with variables and methods
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# bobject=B()
# bobject.m1()
# bobject.m2()


#Example3:multiple inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(B):
#     i,j=2,3
#     def m3(self):
#         print(self.i*self.j)
# class D(C):
#     p,q=4,2
#     def m4(self):
#         print(self.p%self.q)
#
# dobject=D()
# dobject.m1()
# dobject.m2()
# dobject.m3()
# dobject.m4()


#example4:heirarchy inheritence
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A): # B is a child class of A
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# class C(A): #C is a child class of A
#     i,j=2,3
#     def m3(self):
#         print(self.i*self.j)
# bobject=B()
# bobject.m1()
# bobject.m2()
#
# cobject=C()
# cobject.m1()
# cobject.m3()


#Example5:multiple inheritance
# class A: # A is a parent class
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B: #B is a parent class
#     a,b=200,100
#     def m2(self):
#         print(self.a+self.b)
# class C(A,B): #C is achild class of A and B
#     i,j=2,3
#     def m3(self):
#         print(self.i*self.j)
# cobject=C()
# cobject.m1()
# cobject.m2()
# cobject.m3()


# #Example6:calling parent class method using child class using super() keyword
# class A:
#     def m1(self):
#         print("This is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")
#         super().m1()
# bobject=B()
# bobject.m1()


#Example7:
# class A:
#     x,y=10,20
#
# class B(A):
#     a,b=100,200
#     def m1(self,i,j):
#         print(i+j)
#         print(self.a+self.b)
#         print(self.x+self.y)
# bobject=B()
# bobject.m1(1000,2000)


#Example8:overriding varaibles
# class Parent:
#     name="Sudha"
# class Child(Parent):
#     name="Akki"
# cobject=Child()
# print(cobject.name)


#Example9:overriding methods
# class Bank:
#     def rateofinterest(self):
#         return 0
# class Xbank(Bank):
#     def rateofinterest(self):
#         return 10
# class Ybank(Bank):
#     def rateofinterest(self):
#         return 12
# xobject=Xbank()
# print(xobject.rateofinterest())
#
# yobject=Ybank()
# print(yobject.rateofinterest())

#Example9: overloading polymorphism
class calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
calobj=calculation()
calobj.add()
calobj.add(10,20)
calobj.add(100,200,300)



