#composition is a designed principle where a complex class is built by combining simpler independent classes. It allows for greater flexibility and reusability of code, as well as easier maintenance. In composition, a class can contain instances of other classes as its members, rather than inheriting from them. This promotes a "has-a" relationship rather than an "is-a" relationship, which is common in inheritance.
class Tail:
    def wag(self):
        print("Wag wag")
class Dog:
    def __init__(self,name):
        self.name=name
        self.tail=Tail() #composition
    def greet(self):
        print("Woof woof, Happy to see you")
        self.tail.wag()
