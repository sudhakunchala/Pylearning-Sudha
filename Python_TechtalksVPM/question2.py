# Take the below 2 lists as input and print expected output
list1= ["my","name"]
list2 = ["is","Sudha"]

# expected out put should be -- my name is Sudha

#approach1:

list3 =list1+list2
print(list3)
# output is ['my', 'name', 'is', 'Sudha']

#Appr2:
list1.extend(list2)
print(list1)
print(' '.join(list1)) # we can use join to covert list into string


