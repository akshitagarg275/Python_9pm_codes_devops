'''
@classmethod
'''

class Emp:

    # class attribute
    company = "ABC"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company

    def profile(self):
        print(f"Company is : {self.company}, name is: {self.name}, age is : {self.age}")


e1 = Emp("JOhn", 23)
e1.profile()

# Instance attribute
# e1.company = "XYZ"

Emp.changeCompany("SRC")



e1.profile()

e2 = Emp("Jane" , 25)
e2.profile()

