class Student: 
    def __init__(self, id, name, dob): 
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []

    def add_course(self, course): 
        self.courses.append(course)

    def get_course_marks(self, course_id): 
        for course in self.courses: 
            if course.id == course_id: 
                return course.marks
        return None

class Course: 
    def __init__(self, id, name): 
        self.id = id
        self.name = name 
        self.marks = None

    def set_marks(self, marks): 
        self.marks = marks

def input_student_info(): 
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    return Student(id, name, dob)

def input_course_info(): 
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return Course(id, name)

def select_course(student, courses): 
    print("Available courses: ")
    for course in courses: 
        print(course.id, course.name)
    selected_course_id = input("Enter course ID to select: ")
    for course in courses: 
        student.add_course(course)
        break

def input_course_marks(student, course): 
    marks = input(input(f"Enter marks for {student.name} in {course.name}: "))
    course.set_marks(marks)

def list_courses(courses): 
    print("Courses:")
    for course in courses: 
        print(course.id, course.name)

def list_students(students): 
    print("Students:")
    for student in students: 
        print(student.id, student.name)

def show_student_marks(student, course_id): 
    marks = student.get_course_marks(course_id)
    if marks is not None: 
        course_name = [course.name for course in student.courses if course.id == course_id] [0]
        print(f"{student.name}'s mark in {course_name}: {marks}")
    else: 
        print("Nothing to find here.")
    
students = []
courses = []

while True: 
    print("1. Add student\n2. Add course\n3. Select course\n4. Input marks\n5. List courses\n6. List students\n7. Show marks\n8. Exit")
    option = int(input("Choose an option: "))

    if option == 1: 
        students.append(input_student_info())
    elif option == 2: 
        courses.append(input_course_info())
    elif option == 3: 
        student_id = input("Enter student ID: ")
        student = next((s for s in students if s.id == student_id), None)
        if student: 
            select_course(student, courses)
        else: 
            print("Who is this?")
    elif option == 4: 
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        student = next((s for s in students if s.id == student_id), None)
        course = next((c for c in courses if c.id == course_id), None)

        if student and course: 
            input_course_marks(student, course)
        else: 
            print("Err they are not found here.")
    elif option == 5: 
        list_courses(courses)
    elif option == 6: 
        list_students(students)
    elif option == 7: 
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        student = next((s for s in students if s.id == student_id), None)
        if student: 
            show_student_marks(student, course_id)
        else: 
            print("Again, who is this?")
    elif option == 8: 
        break