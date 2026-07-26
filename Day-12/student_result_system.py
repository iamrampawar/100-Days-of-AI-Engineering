class Student():

    def __init__(self,name,branch,marks):
        self.name = name
        self.branch = branch
        self.marks = marks


    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My branch is {self.branch}")
        print(f"My score is {self.marks}")
        print(f"-"*30)


    def cal_grade(self):
        if self.marks>=90:
            print("Your grade is 'A+' ")

        elif self.marks>=80:
            print("Your grade is 'A' ")

        elif self.marks>=70:
            print("your grade is 'B' ")

        elif self.marks>=60:
            print("Your grade is 'C' ")

        else:
            print("You are failed!")
        print("="*30)

        
student1 = Student("Ram","IT",90)
student2 = Student("Krishna","AI",76)
student1.introduce()
student1.cal_grade()

student2.introduce()
student2.cal_grade()