# 5!=1x2x3x4x5=120

n= int(input("enter a number:"))
fact=1

if n<1:
    print("factorial doesnot exist for negative numbers")
elif n==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of a number is:",fact)