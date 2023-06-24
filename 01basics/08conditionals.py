'''
Conditionals: We are going control the flow of statements on the basis of the provided condition

NOTE: indentation -> extra white space which defines the block in Python

only if

if condtion:
    if statements

##########################
    
if else pair

if condition:
    if statements
else:
    else statements

#########################
    
if elif ladder
if condition:
    if statements
elif condition:
    elif statement
elif condition:
    elif statement
    .
    .
    .
    .
    .
else:
    else statements
'''

# weather = "rain"

# weather = input("Please enter the weather: ")

# if weather == "rain":
#     print("Take the umbrella")

# if weather == "rain":
#     print("Take the umbrella")
# else:
#     print("Do not take umbrella")

# print("other lines of code")

# if weather == "summer":
#     print("It's summer!")
# elif weather == "winter":
#     print("It's winter!")
# elif weather == "rainy":
#     print("It's raining!")
# else:
#     print("Enter the correct weather")


# if weather == "summer":
#     print("It's summer!")
# if weather == "winter":
#     print("It's winter!")
# if weather == "rainy":
#     print("It's raining!")
# else:
#     print("Not raining")






# whether a person can have a licence

# age = int(input("Please enter your age: "))

# if age >= 18:
#     print("You can have licence")
# else:
#     print("You cannot have the licence")

# WAP to find whether the given number is +ve, -ve or 0

num = int(input("Enter a num: "))

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
elif num < 0 :
    print("Negative")
else:
    print("Enter a valid num")