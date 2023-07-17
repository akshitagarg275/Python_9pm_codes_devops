'''
Inheritance -> Child (derived) class inherits the methods and attributes from base (super) class

single inheritance
multiple inheritance
multilevel inheritance

'''

# TODO: Single Inheritance

class A:
    def greet(self):
        print("I am greet in class A")


class B (A):
    def greet2(self):
        print("I am greet in class B")


# obj = B()
# obj.greet()

# TODO: Multile inheritance
class A:
    def greet(self):
        print("I am greet in class A")


class B:
    def greet(self):
        print("I am greet in class B")

class C (B, A):
    def greet2(self):
        print("I am greet in class C")

# obj = C()
# obj.greet()



# TODO: Multilevel Inheritance
class A:
    def greet(self):
        print("I am greet in class A")


class B(A):
    def greet2(self):
        print("I am greet in class B")

class C (B):
    def greet2(self):
        print("I am greet in class C")

obj = C()
obj.greet()


obj2 = B()
obj2.greet()