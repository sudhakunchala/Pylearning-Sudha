# what is the output of the program?
class A:
    def demo(self):
        print("In class A")
class B(A):
    def demo(self):
        print("In class B")
class C(A):
    def demo(self):
        print("In class C")
class D(B,C):
    pass
test=D()
test.demo()
