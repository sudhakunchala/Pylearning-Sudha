#approch1
# import sys
# sys.path.append("C:/Users/sudha/PycharmProjects/PythonLearning/Day6/package1")
# sys.path.append("C:/Users/sudha/PycharmProjects/PythonLearning/Day6/package1/package2")
#
# import module1
# import module2
#
# module1.display()
# module2.show()


#Approch2
import sys
sys.path.append("C:/Users/sudha/PycharmProjects/PythonLearning/Day6/package1")
sys.path.append("C:/Users/sudha/PycharmProjects/PythonLearning/Day6/package1/package2")

from module1 import *
from module2 import *

display()
show()
