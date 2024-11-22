# A list is a collection which is ordered and manageble
# in python list will be written with square brackets[]
# list is mutable i.e values can change
#

# example1:
#list1=list[10,20,30,40,50]
#list2=list["welcome","sudha","python"]
#list3=list[10,"Sudha",20.5]
#list4=list() # empty list
#print(list1)
#print(list2)
#print(list3)
#print(list4)


#example2: accessing items from the list
# list1=[10,20,30] #index starts from 0
# print(list1[0])
# print(list1[1])
# print(list1[-1]) # returns last value in the list
# print(list1[-2]) # returns next to last value from the list


# example3: you can get multiples indexes using range
# mylist=["Raju", "Sudha","Arjun", "Akshara", "nanna", "amma","brother","sister"]
# print(mylist[2:5]) #returns from the inderx 2 to index 5-1 i.e is 4


#example4: change item values from the list
# mylist=["Raju","Sudha","Arjun"]
# print(mylist)
# mylist[2]="Akshara"  # Arjun is replaced with Akshara
# print(mylist)


#example5: read the values in the list by looping statement
# mylist=["Raju", "Sudha","Arjun", "Akshara", "nanna", "amma","brother","sister"]
# for i in mylist:
#     print(i)


#example6:check if the item is present in the list or not
# mylist=["Raju", "Sudha","Arjun", "Akshara", "nanna", "amma","brother","sister"]
# if "Raju" in mylist:
#     print("present")
# else:
#     print("not present")

#example7:to know the count ( length of the list) we use len()
# mylist=["Raju", "Sudha","Arjun", "Akshara", "nanna", "amma","brother","sister"]
# print(len(mylist))


#example8: adding new items to the list
#append() : it will add the new item in the ending of the list
#insert(): it will add the new item in the middle of the list , insert(index, new item)

# mylist=["Raju", "Sudha","Arjun", "Akshara", "nanna", "amma","brother","sister"]
# mylist.append("akki")
# print(mylist)
# mylist.insert(4,"Ajju")
# print(mylist)


#example9: how to remove item from the list
# pop() : we can delete from the list
# mylist=["Apple", "Banana","Mango", "Kiwi"]
# mylist.pop(1) # you need to specify index number of the item to be deleted
# print(mylist)

# we can delete using del keyword
# mylist=["Apple", "Banana","Mango", "Kiwi"]
# del mylist[1]
# print(mylist)


# if you want to delete all the items from the list , use clear()
# mylist=["Apple", "Banana","Mango", "Kiwi"]
# mylist.clear()
# print(mylist) # returns empty list

#example10: how to copy 1 list into another list using list()
# A=["Apple", "Banana","Mango", "Kiwi"]
# B= list(A)
# print(A)
# print(B)

#emaple11: cpy list using copy()
# A=["Apple", "Banana","Mango", "Kiwi"]
# B= A.copy()
# print(A)
# print(B)

#Example12: join 2 lists
# using + operator
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3)


#using loop statement how to joing two lists
# list1=["a","b","c"]
# list2=[1,2,3]
# for i in list2:
#     list1.append(i)
# print(list1)

#using extend() how to join two lists
list1=["a","b","c"]
list2=[1,2,3]
list1.extend(list2)
print(list1)


