# write a python program to count the number of times a class is called?
# or How to count number of instances of  a class in python?

class A:
    count=0
    def __init__(self):
        A.count+=1
        print("Class A is called")
a1=A()
a2=A()
a3=A()
print(A.count)


#Approach2: using global variable

count=0
class B:

    def __init__(self):
        global count
        count +=1
        print("Class B is called")
b1=B()
b2=B()
print(count)