'''
List comprehension
'''
# l = []
# for i in range(5):
#     l.append(i)

# print(l)

# l = [i for i in range(5)]
# print(l)

# TODO: using if
# list of evens

# even = [i for i in range(10) if i%2 == 0]
# print(even)

# TODO: using if and else
nums = [(i**2) if i%2 ==0 else i**3 for i in range(10)]
print(nums)