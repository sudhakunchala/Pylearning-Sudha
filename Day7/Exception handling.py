# Exception is an event which will cause program termination
# In python , we can handle exceptions using try, except ,else

# print("This is a starting line of a program")
# print("This is a starting line of a program")
# print("This is a starting line of a program")
# try:
#     print(x) # x is not defined, so throws exception and terminate the program from here, to handle this we use try and except
# except:
#     print("exception occured")
# print("This is a ending line of a program")
# print("This is a ending line of a program")
# print("This is a ending line of a program")



#Example2:using try,except,else ,finally
try:
    num1,num2=10,5
    result=num1/num2
    print("result is:",result)
except:
    print("exception thrown")
else:
    print("exception handled")
finally:
    print("always executed..")



