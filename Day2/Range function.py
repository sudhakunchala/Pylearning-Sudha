# range() function is used to give the values in the range
# to use range () , we need use with list() function to get the values in the range()
# list(range(10))...return the values from 0to 9
#list(range(0,10))..return starting number from 0 and ending number 10-1, i.e 9
#list(range(0,10,2)...returns starting number 0 and ending number 9, and it will give the number by adding 2 to each number

print(list(range(10))) # 0,1,2,3,4,5,6,7,8,9
print(list(range(2,10))) # 2,3,4,5,6,7,8,9
print(list(range(0,10,2))) #0,2,4,6,8
print(list(range(-10,1)))
print(list(range(-10,1,2)))