#Sorting works differently for numbers and strings,
# but Python’s built-in sorted() function and .sort() method handle both efficiently.

# sorting a list of numbers
# list=[2,5,7,3,6,9,1,6,0]
# list.sort() # sort in ascending order
# print(list)

#approach2: using sorted()
# list=[3,5,1,7,9,0,4,5,]
# sorted_list=sorted(list)
# print(sorted_list)

#sorting strings
# list=["apple","dog","banana","eagle","cherry"]
# list.sort()
# print(list)

# case insensitive :key=str.lower
# list=["apple","Dog","banana","Eagle","cherry"]
# list.sort(key=str.lower)
# print(list)

#numbers sorting in descending order
# list=[3,5,1,2,8,0,6,2,9]
# list.sort(reverse=True)
# print(list)

#mixed list sorting
list=["apple",1,6,9,"cherry","banana"]
list.sort(key=str)
print(list)