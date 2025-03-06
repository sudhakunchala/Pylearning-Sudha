#write a one line for loop to print all the words in the below list which starts with the character 'i'
# list= ['india', 'is', 'my, 'country']
#expected output = 'india','is'

list1= ['india', 'is', 'my', 'country']
list2 = [word for word in list1 if word.startswith('i')]
print(list2)

