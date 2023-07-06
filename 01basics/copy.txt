'''
DRY -> Donot Repeat Yourself
functions -> wrapping a certain set of code which can reused

def function_name (parameters):
    //function statements

'''

# function definition
def greeting():
    print("Hello")
    

# calling
# greeting()
# greeting()

# add function
def addition(num1 , num2):
    sum = num1 + num2
    print("sum is: ", sum)

# addition(3, 4)

# return 

def calc (num1 , num2):
    sum = num1 + num2
    sub = num1 - num2
    return sum, sub

# print(calc(5 , 6))

# ans = calc(2,3)
# print("add is :" , ans[0])
# print("sub is :" , ans[1])


# default arguments

# def profile (name = "NA" , age = "NA"):
#     print(f"name is : {name} and age is : {age}")

# default arguments should always follow non-default argument
def profile (name  , age = "NA"):
    print(f"name is : {name} and age is : {age}")

# profile("John")
# profile("Jane" , 23)
# profile()

n = "Rahul"
a = 24
# profile(n , a)

# positional(keywords) arguments

def profile (name  , age = "NA"):
    print(f"name is : {name} and age is : {age}")

# profile(age = 23 , name = "John")

# variable length arguments
# *args

def func (a, b, *args):
    print("a val is: ",a)
    print("b val is: ",b)
    # print(args)
    # print(type(args))

    for i in args:
        print(i)

# func(1,2,34,5,6,6)
# func(2,3)



# variable length keyword arguments
# **kwargs

def func2 (**kwargs):
    print(kwargs)
    print(type(kwargs))

# func2(fname = "John" , lname = "Doe", age = 23)

def func3(name, *args , **kwargs):
    print(name)
    print(args)
    print(kwargs)

# func3("John")
# func3("John", 23)
# func3("John", 23, course="Python")



# lambda functions -> anonymous functions
# one line functions
# no return or def keyword
# lambda parameters : expression

sqr = lambda num : num **2

# print(sqr(5))

# lambda <arguments> : <statement1> if <condition> else <statement2>

eve_odd = lambda num : "even" if num%2 ==0 else "odd"

# print(eve_odd (23))


# Applications of Lambda functions

# map -> to create a new list from exisitng one on the basis of certain condition

nums = [1,2,3,4,5,6]
# sqr = list(map(lambda num : num **2 , nums))
# print(sqr)

# filter -> filters out the data on the basis of the condition
# even = list(filter(lambda num : num % 2 == 0 , nums))
# print(even)

# reduce
from functools import reduce

ans = reduce(lambda a,b : a+b , nums)
print(ans)


