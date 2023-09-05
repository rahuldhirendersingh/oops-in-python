class Computer:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        
    def config(self):
        print("Config is", self.cpu, self.ram)
        
        
com1 = Computer('intel i5', '16gb')
com2 = Computer('ryzen 5', '32gb')

com1.config()
com2.config()

