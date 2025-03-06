# combine 2 lists and convert it to a dictionary as shown below
list1= ['a','b','c']
list2=[1,2,3]

# expected output = {'a':1, 'b':2 , 'c':3}

# Appr1:
dict1 = dict(zip(list1,list2)) # we can use dict(zip(list1,list2)) combines two lists and coverts into dictionary
print(dict1)

# appr2:

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2)

