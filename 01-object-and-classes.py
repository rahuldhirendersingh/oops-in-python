
class Computer:
    
    def config(self):
        print('i5', '16gb', '1TB')
    

x = 5
print(type(x))

a = '5'
print(type(a))

com1 = Computer()
com2 = Computer()
print(type(com1))


# how to call the function, config?

# config() # error: in order to access the function you need to mention the class name first.

# Computer.config() # no argument passed for the self argument.

'''
Why using self parameter?

- So the thing is there are more than one object of a class at most case when you call the method of the class for which object are you calling the method.

-It's like you got a human class and it has two object, ajay and arjun, when you say hey human run, which human is supposed to run, arun or arjun. In short to call a method you need to tell which object is support to run the method.
'''

Computer.config(com1)
Computer.config(com2)

com1.config() # it will automatically take comp1 in self as an argument.
com2.config() 