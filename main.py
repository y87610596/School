
class Student:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

class Teacher:
    def __init__(self, first_name, last_name, subject, classes):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes = classes

class HomeroomTeacher:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

students = []
teachers = []
homeroom_teachers = []

def create_user():
    user_type = input("Enter the user type (student, teacher, homeroom teacher, end): ")

    if user_type == "student":
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        class_name = input("Enter student's class name: ")
        student = Student(first_name, last_name, class_name)
        students.append(student)

    elif user_type == "teacher":
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        subject = input("Enter the subject taught by the teacher: ")
        classes = []
        while True:
            class_name = input("Enter a class taught by the teacher (or type end to finish): ")
            if class_name == "end":
                break
            classes.append(class_name)
        teacher = Teacher(first_name, last_name, subject, classes)
        teachers.append(teacher)

    elif user_type == "homeroom teacher":
        first_name = input("Enter homeroom teacher's first name: ")
        last_name = input("Enter homeroom teacher's last name: ")
        class_name = input("Enter the class led by the homeroom teacher: ")
        homeroom_teacher = HomeroomTeacher(first_name, last_name, class_name)
        homeroom_teachers.append(homeroom_teacher)

    elif user_type == "end":
        return

def manage_users():
    manage_option = input("Enter a user type to manage (class, student, teacher, homeroom teacher, end): ")

    if manage_option == "class":
        class_name = input("Enter the class name: ")
        print("Students in the class:")
        for student in students:
            if student.class_name == class_name:
                print(f"{student.first_name} {student.last_name}")
        print("Homeroom teacher:")
        for homeroom_teacher in homeroom_teachers:
            if homeroom_teacher.class_name == class_name:
                print(f"{homeroom_teacher.first_name} {homeroom_teacher.last_name}")

    elif manage_option == "student":
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        for student in students:
            if student.first_name == first_name and student.last_name == last_name:
                print("Class of the student:")
                print(student.class_name)
                for teacher in teachers:
                    if student.class_name in teacher.classes:
                        print(f"{teacher.first_name} {teacher.last_name}. Subject:{teacher.subject}")

    elif manage_option == "teacher":
        first_name = input("Enter teacher's first name: ")
        last_name = input("Enter teacher's last name: ")
        print("Classes taught by the teacher:")
        for teacher in teachers:
            if teacher.first_name == first_name and teacher.last_name == last_name:
                for class_name in teacher.classes:
                    print(class_name)

    elif manage_option == "homeroom teacher":
        first_name = input("Enter homeroom teacher's first name: ")
        last_name = input("Enter homeroom teacher's last name: ")
        print("Students led by the homeroom teacher:")
        for homeroom_teacher in homeroom_teachers:
            if homeroom_teacher.first_name == first_name and homeroom_teacher.last_name == last_name:
                for student in students:
                    if student.class_name == homeroom_teacher.class_name:
                        print(f"{student.first_name} {student.last_name}")

    elif manage_option == "end":
        return

while True:
    print("Available commands: create, manage, end")
    command = input("Enter a command: ")

    if command == "create":
        create_user()

    elif command == "manage":
        manage_users()

    elif command == "end":
        break