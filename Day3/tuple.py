# A tuple is a collection which is ordered and manageble
# in python tuple will be written with ()
# list is immutable i.e values can't change

#Example1: to create tuple
# mytuple=(10,20,30,40,50)
# print(mytuple)

# mytuple=("apple","banana","kiwi")
# print(mytuple)

#Example2:to access tuple items
# mytuple=("apple","banana","kiwi")
# print(mytuple[1])

#Example3:range of indexes
# mytuple=("apple","banana","kiwi","mango","cherry","strawberry")
# print(mytuple[1:5])


# Tuple is a immutable
# we cannot modify existing value
# we cannot append new value
# we cannot insert a new value
# we cannot remove a value


#Example4:changing tuple values
#bydefault we can't change tuple values, because tuple is immutable
#but there is a workaround
#tuple-->list(modify)--->tuple

# mytuple=("Apple","Mango","Banana")
# print(mytuple)
# mylist=list(mytuple)
# print(mylist)
# mylist[1]="Orange"
# mytuple=tuple(mylist)
# print(mytuple)


#example5:reading items in the tuple using looping
mytuple=("Apple","Mango","Banana")

for i in mytuple:
    print(i)





