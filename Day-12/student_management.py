class Student():

    
    def __init__(self,name,age,branch,cgpa):
        self.name = name
        self.age = age
        self.branch = branch
        self.cgpa = cgpa

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"My branch is {self.branch}")
        print(f"My CGPA is {self.cgpa}")
        print("-"*30)

student1 = Student("Ram",20,"IT",7.19)
student2 = Student("Krishna",21,"AI",8.50)
student1.introduce()
student2.introduce()