# number should be greater than 1
# prime number should have 2 factors, 1 and number itself

num= int(input("enter a number:"))
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i==0):
            count=count+1
    if count==2:
        print("prime number:",num)
    else:
        print("not prime:",num)

