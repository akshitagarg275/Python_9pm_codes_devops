'''
Multiple Inheritance -> One child class is inheriting from multiple parent class
'''

class Human:
    def breathe(self):
        print("I do breathe!")

class Employee:
    def onboarding(self):
        print("Welcome on board!")

    def breathe(self):
        print("I am surviving")

class Programmer(Employee, Human):
    def debug(self):
        print("I am debugging!!")

p1 = Programmer()
p1.breathe()