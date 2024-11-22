# class myclass:
#     def myfunc(self): # Whenever we create method inside a class, it will pass Self argument ny default
#         pass
#     def display(self):
#         print("Sudha")
#
# mc1=myclass()
# mc1.myfunc()
# mc1.display()


#Example2:
#2 typeas of methods we can define within the class
#1.Instance method:we can call only through object
#2.static method: we can directly call using class

# class myclass():
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,num):
#         print(self,num)
# mc=myclass()
# mc.m1()
# mc.m2(100,200)
# myclass.m2(10,20) # static method we can call using class not object


# Example3: using class variables
# class myclass:
#     a,b=10,20 # these are the class variables
#     def add(self):
#         print(self.a+self.b) #if you want to use class variable within the methos, we need to use self keyword
#     def mul(self):
#         print(self.a*self.b)
# mc=myclass()
# mc.add()
# mc.mul()


#Example4: using local,global and class variables
# i,j=10,20
# class myclass:
#     x,y=100,200
#     def add(self,a,b): #a,b are local variables
#         print(a+b)
#         print(self.x+self.y)  #x,y are class variables
#         print(i+j) #i,j are global variables
# mc=myclass()
# mc.add(1000,2000)



#Example5: using local,global and class variables with same names
# a,b=10,20
# class myclass:
#     a,b=100,200
#     def add(self,a,b): #a,b are local variables
#         print(a+b)
#         print(self.a+self.b)  #a,b are class variables
#         print(globals()['a']+globals()['b']) #a,b are global variables
# mc=myclass()
# mc.add(1000,2000)

#Example6: multiple objects for 1 single class
# class myclass():
#     def display(self,name):
#         print(name)
#         print("this is display method")
# mc1=myclass()
# mc1.display("sudha")
#
# mc2=myclass()
# mc2.display("Akki")


#Example6:Constructor
# class myclass:
#     def __init__(self):
#         print("This is a constructor")
#     def m1(self):
#         print("Sudha")
# mc=myclass() # whenever we create object , constructor will invoke automatically, no need to call
# mc.m1()


#Example7: constructor with passing argument
class myclass:
    name="Sudha"
    def __init__(self,name):
        print(name)
        print(self.name)
mc=myclass("Akki")




