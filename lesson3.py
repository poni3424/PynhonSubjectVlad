class Student:
    print("Hi")
    def __init__(self,name,age,numberPhone):
        self.name = name
        self.age = age
        self.numberPhone = numberPhone

    def printer(self):
            print("Name of student", self.name)
            print("Name of student", self.age)
            print("Name of student", self.numberPhone)
    def calculateSeconds(self):
        print("Seconds which student life",self.age*365*24*60*68)


frist_student = Student("Vlad",13, "+48792313122")
frist_student.printer()
frist_student.calculateSeconds()
print()
print()

second_student = Student("Andrew", 23, "+48222222222")
second_student.printer()
second_student.calculateSeconds()
