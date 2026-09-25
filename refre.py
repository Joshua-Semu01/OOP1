class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p1 = Person("Alice", 30)
p1.greet()  

class phone:
    def __init__(self,brand,At):
        self.brand=brand
        self.At=At
    def load_At(self,amount):
        self.At=self.At + amount
a=phone("Samsung",100)
b=phone("Iphone",200)
a.load_At(50)
print(a.At)