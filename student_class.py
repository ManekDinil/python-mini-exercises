class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade 

  def get_details(self):
    print (f"Student:{self.name}\nage:{self.age}\ngrade:{self.grade}")

student1 = Student("Ram", 22, 90)
student1.get_details()