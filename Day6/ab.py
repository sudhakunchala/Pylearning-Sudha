# we need call classs from a and b in ab.py
# #approch1
# import a
# import b
# obj1=a.Animal()
# obj1.display()
#
# obj2=b.Bird()
# obj2.display()


#approch2
from a import Animal
from b import Bird
obj1= Animal()
obj1.display()

obj2=Bird()
obj2.display()