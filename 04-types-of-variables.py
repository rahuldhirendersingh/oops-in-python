
class Car:
    
    wheels = 4 # class[static] variable
    
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'
        

c1 = Car()
c2 = Car()

c1.mil = 8 # instance variable
Car.wheels = 6 # - would change for all the objects.

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


'''
Instance Variable.

- instance variable's are different for different objects and if you change one it would not affect the other objects.

Class Variable.

- class variable is same for all object means all object are going to use the same variable and if you change the class variable the value will be changed for all the objects.
'''
