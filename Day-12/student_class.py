class Student:

    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.branch = branch

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} Years old")
        print(f"My branch is {self.branch}")

student1 = Student("Ram",20,"IT")

student1.introduce()