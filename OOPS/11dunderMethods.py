class Num:
    """This is a num class"""
    def __init__(self, n) :

        self.num = n
    
    def __add__(self, ob):
        return self.num + ob.num
    
    def __str__(self):
        return f"I am an object of Num class having value {self.num}"
    
    def __lt__(self, ob):
        return self.num < ob.num

obj = Num(2)
# help(Num)

obj2 = Num(3)

# print(obj + obj2)
# print(obj)

# print(obj < obj2)

class Values:

    def __init__(self,nums):
        self.nums=nums
    
    def __len__(self):
        return len(self.nums)


obj3=Values([1,2,3,4,5,6])

# print(len(obj3.nums))
print(len(obj3))