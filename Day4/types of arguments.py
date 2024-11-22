# def myfunc(a,b,c):
#     print(a,b,c)
# myfunc(10,20,30) # positional argumnets
# myfunc(a=10,b=20,c=30)    # keyword argumnets
# myfunc(10,b=20,c=30)    # combination of positional and keyword arguments
# myfunc(a=10,20,30)  # invalid , because positional argument must appear before keyword argument


# example2: functions can return many values
def largest(a,b):
    if a>b:
        return(a,b)
    else:
        return(b,a)
print(largest(10,20))