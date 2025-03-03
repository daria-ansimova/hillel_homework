class UserError(Exception):
    def __init__(self, message="Cannot add more than 10 students to the group\n"):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise UserError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '

students = [
    Student('Male', 30, 'Steve', 'Jobs', 'AN142'),
    Student('Female', 25, 'Liza', 'Taylor', 'AN145'),
    Student('Male', 22, 'John', 'Doe', 'AN143'),
    Student('Female', 23, 'Jane', 'Doe', 'AN144'),
    Student('Male', 24, 'Bob', 'Smith', 'AN146'),
    Student('Female', 25, 'Alice', 'Johnson', 'AN147'),
    Student('Male', 26, 'Charlie', 'Brown', 'AN148'),
    Student('Female', 27, 'Eva', 'Green', 'AN149'),
    Student('Male', 28, 'George', 'White', 'AN150'),
    Student('Female', 29, 'Hannah', 'Black', 'AN151'),
    Student('Male', 30, 'Ian', 'Gray', 'AN152'),
]

gr = Group('PD1\n')

for student in students:
    try:
        gr.add_student(student)
        print(f"Added: {student.first_name} {student.last_name}")
    except UserError as e:
        print(e)

# print(gr)
assert str(gr.find_student('Jobs')) == str(students[0]), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!