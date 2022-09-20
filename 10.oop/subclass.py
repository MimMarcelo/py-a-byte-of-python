class SchoolMember:
    """Representa um membro da escola"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized SchoolMember: {self.name}", end=" ")

    def tell(self):
        """Informar meus detalhes"""
        print(f"\nName: {self.name}\nAge: {self.age}")

class Teacher(SchoolMember):
    """Representa um professor"""
    
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("as a teacher")
    
    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: R$ {self.salary}\n")

class Student(SchoolMember):
    """Representa um estudante"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("as a student")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Marks: {self.marks}\n")

t = Teacher("Mrs. Shrividya", 40, 3000)
s = Student("Marcelo", 25, 75)

members = [t, s]

for member in members:
    member.tell()