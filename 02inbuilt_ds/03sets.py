'''
sets -> collection of particular category
set()
{}
No indexing : these do not have any fixed position
iterable
IT doesnot have the duplicate values
'''

a = {1,2,3,45,65,3}
# print(a)
# print(type(a))

# a.add(55)
# print(a)

# TODO: if that particular element do not exist , it will not throw any error
# a.discard(31)
# print(a)

# TODO: if that particular element do not exist , it gives KeyError
# a.remove(31)


a = {1,2,3,4}
b= {3,4,5,6}

# TODO: Union
# print(a.union(b))
# print(a | b)

# TODO: intersection
# print(a.intersection(b))
# print(a & b)

# TODO: difference
print(a.difference(b))
print(a - b)

print(b.difference(a))
print(b - a)

