'''
Constructor -> It is a special method which gets called as soon as an object of the class is created

def __init__():

'''

class Employee:

    def __init__(self, n , age = "NA"):
        self.name = n
        self.age = age
        print("Constructor called!!")

    def getName(self):
        return self.name , self.age

obj = Employee("John", 23)
print(obj.getName())

obj2 = Employee("Jane")
print(obj2.getName())