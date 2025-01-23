import pytest
#how to delete the key from dictionary
# my_dic={'a':1,'b':2,'c':3}
# print(my_dic)
# del my_dic['b']
# print(my_dic)

# difference between list and tuple
# list= ["Apple","Banana","Cherry"]
# print(list[0]) # output is Apple
# list.append("Orange") # adding
# print(list)
# list[1]= "Strawberry" # change
# print(list)

#tuple
# tuple=("Sudha","Arjun","Raju","Akki")
# print(tuple)
# print(tuple[0])

# finding an element in the list, we use 'in' operator
# list=[1,2,3,"Arjun","AKKI",5,6,7]
# if 10 in list:
#     print("True")
# else:
#     print("False")


# parametirize in pytest

@pytest.mark.parametirize("input,expected",[(1,2),(2,3),(3,4)])

def test_increment(input,expected):
    assert input+1==expected


# how to download webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()

driver.find_element(By.ID,"value")