'''
Scope: In the program where it has the life
global
local
'''
# global
a = 10

def inner():
    # local
    # a =20
    global a
    a = 30
    print("inner: ",a)

print("Outer: ",a)


inner()
print("Outer after: ",a)