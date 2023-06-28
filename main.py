students = {}
teachers_subject = {}
teachers_cls = {}
homeroom_teachers = {}

def create_user():
    user_type = input("Enter the user type (student, teacher, homeroom teacher, end): ")

    if user_type == "student":
        student_name = input("Enter the student's name: ")
        class_name = input("Enter the class name: ")
        students[student_name] = class_name
    elif user_type == "teacher":
        teacher_name = input("Enter the teacher's name: ")
        subject = input("Enter a subject: ")
        teachers_subject[teacher_name] = subject
        clss = []
        while True:
            cls = input("Enter classes this teacher teach (leave empty to finish): ")
            if not cls:
                break
            clss.append(cls)
        teachers_cls[teacher_name] = clss

    elif user_type == "homeroom teacher":
        teacher_name = input("Enter the homeroom teacher's name: ")
        class_name = input("Enter the class name: ")
        homeroom_teachers[teacher_name] = class_name
    elif user_type == "end":
        return

def manage_users():
    manage_option = input("Enter a user type to manage (class, student, teacher, homeroom teacher, end): ")

    if manage_option == "class":
        class_name = input("Enter the class name: ")
        print("Students in the class:")
        for student, cls_name in students.items():
            if cls_name == class_name:
                print(student)
        print("Homeroom teacher:")
        for teacher, cls_name in homeroom_teachers.items():
            if cls_name == class_name:
                print(teacher)

    elif manage_option == "student":
        student_name = input("Enter the student's name: ")
        print("Classes attended by the student:")
        for student, cls_name in students.items():
            if student == student_name:
                print(cls_name)
        print("Teachers of the classes:")
        for teacher, classes in teachers_cls.items():
            if students.get(student_name) in classes:
                print(teacher)

    elif manage_option == "teacher":
        teacher_name = input("Enter the teacher's name: ")
        print("Classes taught by the teacher:")
        for teacher, classes in teachers_cls.items():
            if teacher == teacher_name:
                print(classes)

    elif manage_option == "homeroom teacher":
        teacher_name = input("Enter the homeroom teacher's name: ")
        print("Students led by the homeroom teacher:")
        for teacher, cls_name in homeroom_teachers.items():
            if teacher == teacher_name:
                for student, cls_name in students.items():
                    if cls_name == cls_name:
                        print(student)

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