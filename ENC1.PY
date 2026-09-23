class StudentGPA:
    def __init__(self, name, starting_gpa):
      self.name = name 
      self._gpa = 0.0 
      self.set_gpa(starting_gpa)

    def is_valid(self, value):
       return 0.0 <= value <= 5.0

    def get_gpa(self): 
       return self._gpa

    def set_gpa(self, new_value):
       if self.is_valid(new_value):
        self._gpa = new_value
        return True
        return False


s1 = StudentGPA("Josh", 4.2)
print(s1.get_gpa()) 
s1.set_gpa(6.0)
print(s1.get_gpa()) 