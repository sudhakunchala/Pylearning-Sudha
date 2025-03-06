# 0,1,1,2,3,5,8..

n1=0
n2=1

print(n1)
print(n2)

for i in range(2,10):
    sum=n1+n2 #1
    print(sum) #1
    n1=n2
    n2=sum


