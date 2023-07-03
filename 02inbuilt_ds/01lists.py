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

# TODO: extend -> To add more than 1 element in the list
# fruits = ["mango", "pineapple", "apple", "guava", "orange"]
# fruits.extend(["plum","pear"])
# print(fruits)

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

# fruits.clear()
# print(fruits)


# TODO: index(element, start, end)
# fruits = ["mango", "pineapple", "apple", "guava", "orange"]
# print(fruits.index("apple"))

# TODO: Will be giving error as we are searching after 3rd index
# print(fruits.index("apple", 3))

# fruits.insert( 2, "plum")
# print(fruits)

# print("BEFORE: ", fruits)
# fruits.remove("apple")
# print("AFTER: ", fruits)

# TODO: reversing the entire list
# print("BEFORE: ", fruits)
# fruits.reverse()
# print("AFTER: ", fruits)

# TODO: sort 
# print("BEFORE: ", fruits)
# # ascending order
# fruits.sort()
# # TODO: descending order
# fruits.sort(reverse=True)
# print("AFTER: ", fruits)

# print(sorted(fruits))
# fruits = sorted(fruits)
# print(fruits)

# TODO: copy

# fruits1 = fruits.copy()
# fruits[0] = "pear"
# print("Fruits: ", fruits)
# print("Fruits1: ", fruits1)

import copy

list1 = [ 1, [2, 3] , 4 ]
list2 = list1
list4 = copy.deepcopy(list1)

list1.append(5)
list1[1][1] = 999

print("List 1: ",list1)
print("List 2: ",list2)




