class Person():
    #Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Method
    def greet(self):
        print(f"Hi {self.name}! You are {self.age} years old.")

#Create instances of the class
alice = Person('Alice',20)
bob=Person('Bob',42)
candice=('Candice',29)

print(alice.name)
print(alice.age)

bob.greet()

    # def __str__(self):
    #     return f"{self.name}, {self.age} years old"
    
    # def greet(self):
    #     return f"Hello, my name is {self.name}"