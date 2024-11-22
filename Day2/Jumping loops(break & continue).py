#jumping statements
#break
#continue
#break will use with if condition
# if you want to break the loop in the middle, then we can use break

# print numbers 1 to 10, and break at 5
for i in range(1,10):
    if i==5:
        break
    print(i)

#continue--if you want to skip the numbers then use continue
for i in range(1,10):
    if i==5:
        continue
    print(i) # 5 is skipped

 # skip multiple numbers
for i in range(1, 10):
    if i == 5 or i==3 or i==7:
        continue
    print(i)