
# class Computer:
#     pass


# c1 = Computer()
# c2 = Computer()
# print(id(c1))
# print(id(c2))

'''
 - Everytime you create a different object it take's a different space that's why both got different id's.
 - Size of the object depends on the no. of variable's and size of each variable.
 - Who allocate size to object? --> Constructor
'''


class Computer:
    
    def __init__(self):
        self.name = "John"
        self.age = 30

    def update(self):
        self.age = 40
        
    def compare(self, other):
        if self.age == other.age:
            return True
        return False

p1 = Computer()
p2 = Computer()

p2.name = "David"
p2.update()

# Use of self

'''
When you call the updare method how would it know which object it has to update, because it only got one parameter than is self so, when you call the function you're passing p2 with it so, the p2 will be passed in self and then p2's age will be changed.
'''

print(p1.name)
print(p2.name)

print(p1.age)
print(p2.age)

# Comparing their age.

if p1.compare(p2):
    print("They are same.")
else:
    print("They are different.")