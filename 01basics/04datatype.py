'''
Datatypes 

'''

#Numeric

#Int -> It stores +ve, -ve and 0
# age = 23
# print("Age is : ",age)
# print("Type of age is: ",type(age))
# print("ID of age variable is: ", id(age))

# Float (decimal)
# price = 23.75
# print("Price is : ",price)
# print("Type of price is: ",type(price))

# Complex (real number +/- imaginary part)
# 5 + 3j
# complex_num = 2 + 3j
# print("Complex num is : ",complex_num)
# print("Type of complex_num is: ",type(complex_num))


# Bool -> True/False
# is_valid = True
# print("is this valid: ", is_valid)
# print("type of is_valid is: ", type(is_valid))

# is_login = False
# print("is user logged in: ", is_login)
# print("type of is_login is: ", type(is_login))


# Strings -> anything within single or double quotes

# single line strings -> ' ' or " "
# st = "Lets learn Python"

# print("value in st is :" , st)
# print("type of st is: ", type(st))

# st2 = '"Python is amazing language"'
# # st2 = "Vivek's  Ipad"
# print("value in st is :" , st2)
# print("type of st is: ", type(st2))


# msg = "we are " \
# "learning python"

# msg = """Hi,
# How are youHope all is good?
# """
# print(msg)


# None 
# temp = None
# print("Temp is :", temp)
# print("Type of temp is :",type(temp))

# Derived Dataypes
# store multiple values under a single variable name

'''
( ) -> Paranthesis
{ } -> Curly braces
[ ] -> Square Brackets
'''

# # LIST -> [ ]
# employees = ["John", "Rahul", "Jane", "Sam"]
# print("Employees in company: ",employees)
# print("Type of employees variable is: ", type(employees))


# Tuple -> ( )
# employees = ("John", "Rahul", "Jane", "Sam")
# print("Employees in company: ",employees)
# print("Type of employees variable is: ", type(employees))

# Set -> { }
# employees = {"John", "Rahul", "Jane", "Sam"}
# print("Employees in company: ",employees)
# print("Type of employees variable is: ", type(employees))

# Dict -> {key : value}
# stud = {
#     "name" : "Sam",
#     "class" : "Python",
#     "Gender" : "M",
#     "age" : 24
# }

# print("Details of stud: ",stud)
# print("Type of stud: ",type(stud))


# Range -> generates the value
# range(start, end, step)
# start is inclusive
# end is exclusive
# step is optional, by default step count is 1

# values = list(range(1, 6))
# print("Values is: ", values)
# print("TYpe of values is :", type(values))

# even = tuple(range(0, 11, 2))
# print(even)
# print(type(even))

rev = list(range(10, 0 , -1))
print(rev)
print(type(rev))
