'''
lists -> [ ]
list()
mutable -> it can be changed
iterable -> we can loop over it
indexed -> Each value in the list can be fetch using the index number
'''

fruits = ["mango", "pineapple", "apple", "guava", "orange"]
# print("len of fruits: ", len(fruits))
# print(fruits)
# print(type(fruits))

# fruits[1] = "apple"
# print(fruits)


# TODO: iteration
# for f in fruits:
#     print(f)

# for i in range(len(fruits)):
#     print(f'fruit at index : {i} is {fruits[i]}')

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# TODO: indexing
# print(fruits[0])
# print(fruits[1])

# print(fruits[-1])

# TODO: slicing
# list_name[start_index : end_index : step]
# start_index is inclusive
# end_index is exclusive

# print(fruits[ : : ])
# print(fruits[ : : -1])

# print(fruits[1 : 4])
# print(fruits[-4 : -1])

# print(fruits[0 : 5 : 2])
# print(fruits[ : : 2])

# TODO: append -> adds element at the end
# print("Before: ",fruits)
# fruits.append("grapes")
# print("after: ", fruits)

# TODO: dynamically a user input list
# size = int(input("enter the size of the list: "))
# val = []

# for i in range(size):
#     ele = int(input("Enter the num: "))
#     val.append(ele)
# else:
#     print("list is: ",val)

# print("fruits count is: ",fruits.count("guava"))

# print(fruits.index("mango"))
# print(fruits.index("orange" , 1 , 3))

fruits.clear()
print(fruits)




