# Write a program to print unique characters in a string
#str= 'sudha'
# expected output: udh

str= 'akshara'
unique=[]
for char in str:
    if str.count(char) == 1 and char not in unique:
        unique.append(char)

print(unique)
print(*unique)


