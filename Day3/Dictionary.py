# Dictionary is a collection which is unordered and changeble
# Dictionary is indexed
# Dictionary is mutable
# Dictionary will write in {} , having key and values
# key should be unique
# values can be repeated


#Example1:to create a dictionary
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# print(mydic)

#Example2:accessing items in adictionary
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# print(mydic[1])

#Example3: accessing items in dictionary using get()
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# print(mydic.get(2))


# #Example4:change values in the dictionary
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# print(mydic)
# mydic[2]="b"
# print(mydic)

#Example5:reading items from dictionar using loop
mydic={1:"x",2:"y",3:"Z",4:"a"}
# for i in mydic:
#     print(i) # prints only keys from the dictionary
#
# for i in mydic:
#     print(mydic[i]) # prints only values from the dictionary

# for i,j in mydic.items():
#     print(i,j)  # prints key and values from the dictionary


#example6:check the key is existing in the dictionary or not
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# if 1 in mydic:
#     print("exist")
# else:
#     print("not exist")


#example7:finding total number of items in dictionary
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# print(len(mydic))

#example8:adding items to dictionary
# mydic={1:"x",2:"y",3:"Z",4:"a"}
# mydic[5]="b"
# print(mydic)


#example9:remove item from dictionary:
# using pop() , we can remove
# using del keyword also we can remove
mydic={1:"x",2:"y",3:"Z",4:"a"}
# mydic.pop(1)
# print(mydic)

# del mydic[1]
# print(mydic) # this will delete 1 item

# del mydic
# print(mydic)  # to delete complete dictionary

#example10: copying dictionary
mydic1={1:"x",2:"y",3:"Z",4:"a"}
mydic2=mydic1
print(mydic2)





