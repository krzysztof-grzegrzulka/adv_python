class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


student1 = Student("Jan", 65)
student2 = Student("Janina", 40)

print(student1.is_passed)
print(student2.is_passed)
