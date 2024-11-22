# #Example1: writing data into text file
# file=open("C:/Users/sudha/Desktop/su.txt",'w')
# file.write("This is my first statement\n")
# file.write("This is my second statement\n")
# file.write("This is my third statement\n")
# file.write("This is my first statement\n")
# file.close()
# print("Program finished")


#Example2: reading data from text file
# file=open("C:/Users/sudha/Desktop/su.txt",'r')
# #print(file.read())
# print(file.readline())
# file.close()


#Example3: appending data in the text file
file=open("C:/Users/sudha/Desktop/su.txt",'a')
file.write("\nThis is my fifth line\n")
file.write("This is my sixth line\n")
file.close()
print("program finished")
