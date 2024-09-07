class Student:
    def __init__(self,name,roll_number,grades):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = grades

    def add_grades(self,grade):
        if grade > 0 and grade < 100:
            self.__grades.append(grade)
        else:
            print("Grade must be between 0 and 100")
    def average(self):
        sum = 0
        for grade in self.__grades:
            sum += grade
        return sum/len(self.__grades)
    def display(self):
        print(self.__name)
        print(self.__roll_number)
        print(self.__grades)


student = Student("Bob",141,[10,90,50])
student.display()
print(student.average())
student.add_grades(10)
print(student.average())
student.add_grades(-25)

