
class Student:
    
    school = "MIT"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self): # instance method - as it works with the objects.
        return (self.m1 + self.m2 + self.m3) / 3
    
    # Accessor        
    def get_m1(self):
        return self.m1
    
    # Mutator
    def set_m1(self, value):
        self.m1 = value
        
        
    # class methods.
    @classmethod
    def info(cls):
        return cls.school
    
    # static methods.
    @staticmethod
    def information():
        print("This is student class...")
    

s1 = Student(88,56,45)
s2 = Student(78,65,84)

# print(s1.avg())
# print(s2.avg())

'''
Two types of instance methods.

Accessor :- When you only wanna fetch the value.
Mutator :- When you want to modify the value.
'''

print(Student.info())

Student.information()

'''
So,
- Instance methods work with instance variables.
- Class methods work with class variables.
- Static variable use is when you wanna make something that has 
nothing to do with instance or class variables.
'''
