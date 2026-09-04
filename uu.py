x = "hello world"
print(x)

name = "John"
print(name)

age = input("Enter your age: ")
print(age)

name = input("Enter your name: ")
email = input("Enter your email: ")
print(name)
print(email)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


student1 = Student("Alice", 20)
student2 = Student("Brian", 22)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
student1.introduce()


class Phone:
    def __init__(self, brand, storage):
        self.brand = brand
        self.storage = storage

    def display_info(self):
        print(f"Brand: {self.brand}, Storage: {self.storage}GB")

    def make_call(self, number):
        print(f"Calling {number} from {self.brand}")


phone1 = Phone("Samsung", 128)
phone1.display_info()
phone1.make_call("099999999")


class BankAccount:
    def __init__(self, owner_name, starting_balance=0):
        self.owner = owner_name
        self.__money = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
            return self.__money
        return "Invalid amount"

    def withdraw(self, amount):
        if amount <= self.__money:
            self.__money -= amount
            return self.__money
        return "Insufficient funds"

    def check_balance(self):
        return self.__money


account1 = BankAccount("Alice", 200)
print(account1.owner)
print(account1.check_balance())
print(account1.deposit(50))
print(account1.withdraw(20))
