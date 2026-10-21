class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    @property
    def get_cgpa(self):
        return self.cgpa
s=  Student("John",5.0)
print(s.cgpa)
print(s.name)